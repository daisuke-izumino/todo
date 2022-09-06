from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from typing import List

class Task(BaseModel):
    task_id: int = None

    class Config:
        orm_model = True

class TaskResponse(Task):
    title: str = Field(None, max_length=50)
    text: str = Field(None, max_length=1024)
    created_at: datetime
    updated_at: datetime

class TaskCreate(BaseModel):
    title: str = Field(None, max_length=50)
    text: str = Field(None, max_length=1024)

class TaskDelete(BaseModel):
    task_id: int = None