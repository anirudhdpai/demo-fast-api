from pydantic import BaseModel
from datetime import date

class TaskBase(BaseModel):
    id: int
    name: str
    description: str
    due_date: date

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
