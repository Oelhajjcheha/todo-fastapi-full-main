# Todo FastAPI Application  
A complete backend Todo application built using **FastAPI**, **SQLAlchemy**, and **Pydantic**, following clean architecture principles.  
Includes a full **test suite** using `pytest` and an automated **CI pipeline** using GitHub Actions.

---
## 👤 Author

Omar El Hajj Chehade
IE University 
FastAPI Backend Project  

- UI: http://127.0.0.1:8000/
- API docs: http://127.0.0.1:8000/docs
---

## 🚀 Features

- FastAPI backend with full CRUD operations for Todos  
- Structured architecture: API → Services → Repository → Database  
- SQLAlchemy ORM models  
- Pydantic schemas  
- Test suite using `pytest`  
- Uses an in-memory SQLite test database for isolated testing  
- CI pipeline that runs tests on all pushes to `main`  
- Project diagrams included in `/docs`  
- Clean and professional repository ready for submission  

---

## 📂 Project Structure

```
todo-fastapi-full-main/
│── app/
│   ├── api/
│   │   └── routes.py
│   ├── core/
│   │   └── config.py
│   ├── repositories/
│   │   └── todo_repository.py
│   ├── services/
│   │   └── todo_service.py
│   ├── crud.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── main.py
│
│── docs/
│   ├── architecture-diagram.png
│   └── class-diagram.png
│
│── tests/
│   └── test_todos.py
│
│── .github/
│   └── workflows/
│       └── tests.yml
│
│── requirements.txt
│── README.md
```

---

## 🛠 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Oelhajjcheha/todo-fastapi-full-main.git
cd todo-fastapi-full-main
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Then open:

👉 http://127.0.0.1:8000/docs  
Interactive Swagger API documentation.

---

## 🧪 Running Tests

Run the full test suite:

```bash
pytest -vv
```

Run with coverage:

```bash
pytest --cov=app --cov-report=term-missing
```

All tests should pass successfully.

---

## 🟩 Continuous Integration (GitHub Actions)

Every push to `main` automatically:

1. Checks out code  
2. Installs dependencies  
3. Runs the test suite  

Workflow file:  
`/.github/workflows/tests.yml`

### CI Configuration:

```yaml
name: Run Tests CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.10"

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: pytest -vv
```

View CI results under the **Actions** tab in the GitHub repository.

---

## 📊 Diagrams

Architecture and class diagrams are stored in:

```
/docs/
    architecture-diagram.png
    class-diagram.png
```

These can be referenced in your project report.

---

## 🎯 Summary

This project demonstrates:

- Clean backend architecture  
- Proper API layering (routes → services → repository → database)  
- Automated unit and integration testing  
- CI/CD best practices  
- FastAPI + SQLAlchemy + Pydantic workflow  
- Well-organized repository structure for grading  

---



