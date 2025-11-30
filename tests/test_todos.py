from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine_test = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine_test,
)

# Override dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Create tables
Base.metadata.create_all(bind=engine_test)

client = TestClient(app)

def test_create_todo():
    response = client.post("/todos", json={"title": "Test Todo", "description": "Hello"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Todo"

def test_read_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_single_todo():
    created = client.post("/todos", json={"title": "Single", "description": "One"}).json()
    todo_id = created["id"]

    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["id"] == todo_id

def test_update_todo():
    created = client.post("/todos", json={"title": "Old", "description": "Desc"}).json()
    todo_id = created["id"]

    response = client.put(
        f"/todos/{todo_id}",
        json={"title": "New", "description": "Updated"},
    )
    assert response.status_code == 200
    assert response.json()["title"] == "New"

def test_delete_todo():
    created = client.post("/todos", json={"title": "Delete Me", "description": "Bye"}).json()
    todo_id = created["id"]

    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 200

    # verify it is gone
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 404
