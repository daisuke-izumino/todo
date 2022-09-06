from urllib import response
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from schema import TaskResponse, TaskCreate, TaskDelete
from typing import List
import crud
from db import get_db

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#　ユーザー情報一覧取得
@app.get("/task", response_model=List[TaskResponse])
def get_task_list(db: Session=Depends(get_db)):
    return crud.read_tasks(db=db)

@app.post("/task", response_model=TaskResponse)
def create_task(task_create: TaskCreate, db: Session=Depends(get_db)):
    return crud.create_task(db=db, task_create=task_create)

@app.post("/task/delete")
def delete_task(task_del: TaskDelete, db: Session=Depends(get_db)):
    return crud.delete_task(db=db, task_del=task_del)