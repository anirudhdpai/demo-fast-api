from sqlalchemy import Column, Integer, String, Sequence, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, Sequence("task_id_seq"), primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    due_date = Column(Date)