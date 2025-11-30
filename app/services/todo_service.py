from sqlalchemy.orm import Session
from app.repositories import todo_repository
from app import schemas

def list_todos(db: Session):
    return todo_repository.get_todos(db)

def get_single_todo(db: Session, todo_id: int):
    return todo_repository.get_todo(db, todo_id)

def create_new_todo(db: Session, todo: schemas.TodoCreate):
    return todo_repository.create_todo(db, todo)

def update_existing_todo(db: Session, todo_id: int, todo: schemas.TodoUpdate):
    return todo_repository.update_todo(db, todo_id, todo)

def remove_todo(db: Session, todo_id: int):
    return todo_repository.delete_todo(db, todo_id)
