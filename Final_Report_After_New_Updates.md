# Minimal To-Do Application – SDLC & DevOps  
## Final Refactored Report  
Author: Omar El Hajj Chehade  
Course: DevOps Pipeline Design – Individual Assignment 1  
Date: October 2025

---

# 1. Introduction & Objective

The goal of this project was originally to design a minimal To-Do List Manager application implementing CRUD operations with FastAPI, SQLite, and a small frontend.  
However, the project has now been **fully refactored and modernized** into a clean, scalable, testable backend application with:

- Modular architecture  
- Service and Repository layers  
- Automated test suite using Pytest  
- Continuous Integration via GitHub Actions  
- Clear directory structure  
- Professional documentation  
- In-memory test database  
- Improved maintainability and scalability  

This report explains:

1. What the **original project** contained  
2. The **issues** in the original structure  
3. Exactly **what was changed**  
4. The **final architecture** and DevOps enhancements  

---

# 2. Chosen SDLC Model & Justification

The Agile SDLC model remained the most suitable choice.  
Agile allowed the project to evolve from:

- Basic CRUD  
- To persistent backend  
- To frontend integration  
- To CI workflow  
- To full backend refactoring  

Frequent iterations made it possible to restructure the application, introduce automated testing, and integrate CI/CD without breaking functionality.

---

# 3. SDLC Phases

### **Planning**
Originally targeted CRUD and basic UI.  
Now includes testing, CI integration, and full backend restructuring.

### **Requirements**
Functional:
1. Create tasks  
2. View tasks  
3. Edit/update tasks  
4. Delete tasks  
5. Persist data using SQLite  
6. (NEW) Pass automated tests  
7. (NEW) Run in CI pipeline  

Non-functional:
- <1s response time  
- Modular code  
- Fully testable  
- Container-ready  
- CI-ready  

### **Design**
Original design was minimal (single-file CRUD).  
Now redesigned with **5-layer architecture**:

1. API (Routers)  
2. Services  
3. Repository Layer (DB access)  
4. ORM Models  
5. Database Session Layer  

Also includes updated UML and architecture diagrams.

### **Implementation**
Originally implemented:
- Single-file FastAPI app  
- SQLite database  
- Simple HTML/JS frontend  

Now includes:
- Fully modular backend  
- Separation of concerns  
- Automated testing  
- Dependency overrides  
- In-memory test DB  
- GitHub Actions CI  

### **Testing**
Old method: Manual testing via Swagger and frontend.  
New method: Automated tests using Pytest with:

- Test client  
- In-memory SQLite DB  
- 5 endpoint tests  
- Dependency override for DB isolation  

### **Deployment**
Originally relied only on Dockerfile + local execution.  
Now improved with:

- GitHub Actions CI pipeline  
- Automatic test execution  
- Automated build validation  

---

# 4. Requirements (Updated)

### Functional Requirements  
✔ Create tasks  
✔ View all tasks  
✔ Edit/update tasks  
✔ Delete tasks  
✔ Persist data in SQLite  
✔ **Automated test suite must pass**  
✔ **Project must run clean in CI**  

### Non-Functional  
- Modular and maintainable code  
- Full test isolation (in-memory DB)  
- Consistent execution via CI  
- Documented architecture  

---

# 5. User Stories & Acceptance Criteria

User stories remain similar but now include test automation:

### **User Story 1**
*As a user, I can create tasks.*  
**Acceptance:** Verified via `/todos` POST + pytest automation.

### **User Story 2**
*As a user, I can view all tasks.*  
**Acceptance:** GET `/todos` and automated list test.

### **User Story 3**
*As a user, I can update tasks.*  
**Acceptance:** PUT `/todos/{id}` verified via automated update test.

### **User Story 4**
*As a user, I can delete tasks.*  
**Acceptance:** DELETE `/todos/{id}` + automated test confirming 404 after delete.

---

# 6. Architecture Overview (Updated)

The architecture has been **significantly refactored** from a single-file CRUD design to a clean multi-layer structure:

### **1. API Layer (`app/api/routes.py`)**
Handles all HTTP routes cleanly.

### **2. Services Layer (`app/services/todo_service.py`)**
Contains business logic.

### **3. Repository Layer (`app/repositories/todo_repository.py`)**
Handles database interactions.

### **4. ORM Models (`app/models.py`)**
SQLAlchemy models.

### **5. Database Layer (`app/database.py`)**
Provides DB session + dependency injection.

### **6. Testing Layer (`tests/test_todos.py`)**
Automated endpoint validation with in-memory DB.

### **7. CI Layer (`.github/workflows/tests.yml`)**
Runs test suite automatically on push.

This new structure is scalable, testable, and production-ready.

---

# 7. UML / Class Diagram

Updated class diagram now reflects:

```
Todo
│── id: int
│── title: str
│── description: str
```

This model maps directly to Pydantic schemas:

- `TodoCreate`
- `TodoUpdate`
- `Todo`

And database entity `Todo`.

---

# 8. Implementation Details (Updated)

### Technologies Used
- Python 3.11  
- FastAPI  
- SQLite + SQLAlchemy  
- Pydantic  
- Pytest  
- GitHub Actions  
- HTML/JS Frontend  
- Docker  

### Key Endpoints (Updated Path)
- `GET /todos`  
- `POST /todos`  
- `GET /todos/{id}`  
- `PUT /todos/{id}`  
- `DELETE /todos/{id}`  

### Key New Features
- Service + repository layers  
- Automated testing  
- Test database isolation  
- CI pipeline  

---

# 9. Version Control (Updated)

Version control now includes meaningful commits such as:

1. `refactor: implement layered architecture`  
2. `test: add pytest suite with in-memory DB`  
3. `ci: add GitHub Actions workflow`  
4. `docs: add README and report`  
5. `chore: remove test.db from repo`  

This commit history shows clear progression and DevOps discipline.

---

# 10. Reflection: DevOps Adaptation (Updated)

The updated To-Do backend is fully ready for DevOps adoption.

### Improvements:
- CI pipeline validates code quality  
- Automated testing ensures reliability  
- Refactored architecture simplifies deployments  
- In-memory DB ensures fast testing  
- Code is now production-grade  
- Documentation added for onboarding and maintainability  

Future enhancements:
- CD pipeline (deployment to Render/Railway)
- Docker Compose for multi-service setup  
- Environment-based configuration  

---

# 11. Setup Instructions

### Local Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Access API at:  
http://127.0.0.1:8000/docs

### Testing

```bash
pytest -vv
```

### Docker Setup

```bash
docker build -t todo-fastapi .
docker run -p 8000:8000 todo-fastapi
```

---

# 12. Conclusion

The project evolved from a minimal CRUD application into a fully structured backend with:

- Clean architecture  
- Automated testing  
- CI integration  
- Documentation  
- Maintainable, testable codebase  

This modernized version reflects professional backend development standards and strong DevOps alignment.

---

# 13. References

- FastAPI Documentation  
- SQLAlchemy ORM  
- Python Official Docs  
- Docker Documentation  
- GitHub Actions Documentation  
