from typing import List

from sqlalchemy.orm import Session

from . import models
from .schemas import TaskList, Task


# Create a new task list
def create_task_list(db: Session, name: str):
    task_list = models.TaskList(name=name)
    db.add(task_list)
    db.commit()
    db.refresh(task_list)
    return task_list


# Get a task list by ID
def get_task_list(db: Session, task_list_id: int):
    return db.query(models.TaskList).filter(models.TaskList.id == task_list_id).first()


# Get all task lists
def get_task_lists(db: Session, skip: int = 0, limit: int = 100) -> List[TaskList]:
    return db.query(models.TaskList).offset(skip).limit(limit).all()


# Update a task list
def update_task_list(db: Session, task_list_id: int, name: str):
    task_list = (
        db.query(models.TaskList).filter(models.TaskList.id == task_list_id).first()
    )
    task_list.name = name
    db.commit()
    return task_list


# Delete a task list (soft delete)
def delete_task_list(db: Session, task_list_id: int):
    task_list = (
        db.query(models.TaskList).filter(models.TaskList.id == task_list_id).first()
    )
    task_list.deleted = True
    db.commit()
    return task_list


def get_tasks(
    db: Session, task_list_id: int = None, skip: int = 0, limit: int = 100
) -> List[Task]:
    if task_list_id is not None:
        return (
            db.query(models.Task)
            .filter(models.Task.task_list == task_list_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
    else:
        return db.query(models.Task).offset(skip).limit(limit).all()


def create_task(db: Session, data: dict) -> Task:
    task = models.Task(**data)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_task(db: Session, task_id: int) -> Task:
    return db.query(models.Task).filter(models.Task.id == task_id).first()
