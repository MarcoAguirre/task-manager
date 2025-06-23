from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


class TaskListCreate(BaseModel):
    name: str
    description: Optional[str] = ""


class TaskListResponse(BaseModel):
    id: UUID
    name: str
    description: Optional[str]
    created_at: datetime
    updated_at: datetime
