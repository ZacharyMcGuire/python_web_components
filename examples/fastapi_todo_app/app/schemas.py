from pydantic import BaseModel


class TaskListBase(BaseModel):
    name: str


class TaskListCreate(TaskListBase):
    pass


class TaskList(TaskListBase):
    id: int
    deleted: bool

    class Config:
        from_attributes = True


class TaskBase(BaseModel):
    summary: str
    description: str
    assignee: str
    status: str
    order: int

    task_list_id: int


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    deleted: bool

    class Config:
        from_attributes = True
