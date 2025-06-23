from fastapi import FastAPI
from app.routers import task_list, tasks

from infrastructure.db.base import Base
from infrastructure.db.session import engine
from infrastructure.db import models  # noqa: F401

app = FastAPI()
app.include_router(task_list.router)
app.include_router(tasks.router)


@app.get("/")
def read_root():
    return {"message": "Task Manager API is running"}


Base.metadata.create_all(bind=engine)
