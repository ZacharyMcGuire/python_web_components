from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Boolean,
    Text,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class TaskList(Base):
    __tablename__ = "task_lists"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted = Column(Boolean, default=False)

    tasks = relationship("Task", back_populates="task_list")


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    summary = Column(String, index=True)
    description = Column(String)
    assignee = Column(String)
    status = Column(String)
    order = Column(Integer)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted = Column(Boolean, default=False)

    task_list_id = Column(Integer, ForeignKey("task_lists.id"))
    task_list = relationship("TaskList", back_populates="tasks")
    comments = relationship("Comment", back_populates="task")
    # Comments can be another related model


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    author = Column(String)  # Optional, can be used if you have user authentication
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted = Column(Boolean, default=False)

    task_id = Column(Integer, ForeignKey("tasks.id"))
    task = relationship("Task", back_populates="comments")
