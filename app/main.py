from fastapi import FastAPI

from infrastructure.db.base import Base
from infrastructure.db.session import engine
from infrastructure.db import models

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Task Manager API is running"}

Base.metadata.create_all(bind=engine)
