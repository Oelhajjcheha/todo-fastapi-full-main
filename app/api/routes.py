from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas
from app.services import todo_service

router = APIRouter()

@router.get("/todos")
def list_todos(db: Session = Depends(get_db)):
    return todo_service.list_todos(db)

@router.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = todo_service.get_single_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.post("/todos")
def create(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return todo_service.create_new_todo(db, todo)

@router.put("/todos/{todo_id}")
def update(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    updated = todo_service.update_existing_todo(db, todo_id, todo)
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated

@router.delete("/todos/{todo_id}")
def delete(todo_id: int, db: Session = Depends(get_db)):
    deleted = todo_service.remove_todo(db, todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Deleted successfully"}
