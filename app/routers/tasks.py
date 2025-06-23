from fastapi import APIRouter, status, HTTPException
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from usecases.task.create import CreateTaskUseCase
from usecases.task.update import UpdateTaskUseCase
from usecases.task.delete import DeleteTaskUseCase
from infrastructure.repositories.task import SqlAlchemyTaskRepository

from uuid import UUID

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: UUID):
    repo = SqlAlchemyTaskRepository()
    task = repo.get_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskResponse(**task.model_dump())

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate):
    repo = SqlAlchemyTaskRepository()
    usecase = CreateTaskUseCase(repo)
    task = usecase.execute(
        title=payload.title,
        description=payload.description,
        priority=payload.priority,
        task_list_id=payload.task_list_id,
    )
    return TaskResponse(**task.model_dump())

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: UUID, payload: TaskUpdate):
    repo = SqlAlchemyTaskRepository()
    existing = repo.get_by_id(task_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Task not found")

    updated = existing.model_copy(update=payload.model_dump(exclude_unset=True))
    usecase = UpdateTaskUseCase(repo)
    result = usecase.execute(updated)
    return TaskResponse(**result.model_dump())

@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: UUID):
    repo = SqlAlchemyTaskRepository()
    task = repo.get_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    usecase = DeleteTaskUseCase(repo)
    usecase.execute(task_id)
    return
