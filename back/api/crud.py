
from sqlalchemy.sql import case
from model import TaskTable
from sqlalchemy.orm import Session
from schema import TaskResponse, TaskCreate, TaskDelete

def read_tasks(db: Session):
    task_list = db.query(TaskTable).all()
    response_list = []
    for task in task_list:
        response_list.append(
            TaskResponse(
                task_id=task.task_id,
                title=task.title,
                text=task.text,
                created_at=task.created_at,
                updated_at=task.updated_at
            )
        )
    return response_list

def create_task(task_create: TaskCreate, db: Session):
    task = TaskTable(**task_create.dict())
    db.add(task)
    db.commit()
    response = (
        db.query(TaskTable)
        .filter(TaskTable.text == task.text)
        .filter(TaskTable.title == task.title)
        .first()
    )
    task = TaskResponse(
        task_id=response.task_id,
        title=response.title,
        text=response.text,
        created_at=response.created_at,
        updated_at=response.updated_at
    )
    return task

def delete_task(task_del: TaskDelete, db: Session):
    task = (
        db.query(TaskTable)
        .filter(TaskTable.task_id == task_del.task_id)
        .first()
    )
    db.delete(task)
    db.commit()
    return {"msg": "削除成功しました"}
