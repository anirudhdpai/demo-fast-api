from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import models
import database
import schemas
from models import Task

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'tasks app is running'}

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/", response_model=schemas.Task)
def create_item(item: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_item = models.Task(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    data = db.query(Task).all()
    return data

@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    data = db.query(Task).filter(Task.id == task_id).first()
    return data

@app.put("/tasks/{task_id}")
def update_task(task_id: int, item: schemas.TaskCreate, db: Session = Depends(get_db)):
    data = db.query(Task).filter(Task.id == task_id).first()
    if not data:
        raise HTTPException(status_code=404, detail="Item not found")
    data.name = item.name
    data.description = item.description
    data.due_date = item.due_date
    db.commit()

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    data = db.query(Task).filter(Task.id == task_id).first()
    if not data:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(data)
    db.commit()
    return {"message": "Item deleted"}
 