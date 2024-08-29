from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from typing import List

from . import crud, schemas
from .dependencies import get_db
from . import views

api_router = APIRouter()
html_router = APIRouter()


@api_router.post("/task-lists/", response_model=schemas.TaskList)
def create_task_list(task_list: schemas.TaskListCreate, db: Session = Depends(get_db)):
    return crud.create_task_list(db=db, name=task_list.name)


@api_router.get("/task-lists/", response_model=List[schemas.TaskList])
def read_task_lists(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_task_lists(db, skip=skip, limit=limit)


@api_router.get("/task-lists/{task_list_id}", response_model=schemas.TaskList)
def read_task_list(task_list_id: int, db: Session = Depends(get_db)):
    db_task_list = crud.get_task_list(db, task_list_id=task_list_id)
    if db_task_list is None:
        raise HTTPException(status_code=404, detail="TaskList not found")
    return db_task_list


@api_router.put("/task-lists/{task_list_id}", response_model=schemas.TaskList)
def update_task_list(
    task_list_id: int, task_list: schemas.TaskListCreate, db: Session = Depends(get_db)
):
    db_task_list = crud.update_task_list(
        db, task_list_id=task_list_id, name=task_list.name
    )
    if db_task_list is None:
        raise HTTPException(status_code=404, detail="TaskList not found")
    return db_task_list


@api_router.delete("/task-lists/{task_list_id}", response_model=schemas.TaskList)
def delete_task_list(task_list_id: int, db: Session = Depends(get_db)):
    db_task_list = crud.delete_task_list(db, task_list_id=task_list_id)
    if db_task_list is None:
        raise HTTPException(status_code=404, detail="TaskList not found")
    return db_task_list


@api_router.post("/tasks", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task.dict())


@api_router.get("/tasks", response_model=List[schemas.Task])
def get_tasks(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return crud.get_tasks(db, skip=skip, limit=limit)


@api_router.get("/tasks/{task_id}", response_model=schemas.Task)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return crud.get_task(db, task_id=task_id)


# Return the index html
@html_router.get("/", response_class=HTMLResponse)
def read_root(db: Session = Depends(get_db)):
    return views.index(crud.get_tasks(db))


@html_router.get("/task/{task_id}", response_class=HTMLResponse)
def read_task(response: Response, task_id: int, db: Session = Depends(get_db)):
    response.headers["Hx-Replace-Url"] = "false"
    return views.task_details(crud.get_task(db, task_id=task_id))


@api_router.post("/tasks/sample", response_model=None)
def create_sample_tasks(response: Response, db: Session = Depends(get_db)) -> None:
    """Creates 10 randomly generated tasks."""
    from faker import Faker
    import random

    fake = Faker()

    for _ in range(10):
        crud.create_task(
            db,
            dict(
                summary=fake.sentence(6),
                description="\n".join(fake.paragraphs(5)),
                assignee=fake.name(),
                status="todo",
                order=random.randint(1, 500),
                task_list_id=1,
            ),
        )

    response.headers["HX-Refresh"] = "true"

    return
