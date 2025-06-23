from fastapi import APIRouter, status, HTTPException
from app.schemas.task_list import TaskListCreate, TaskListResponse
from usecases.task_list.create import CreateTaskListUseCase
from usecases.task_list.update import UpdateTaskListUseCase
from usecases.task_list.delete import DeleteTaskListUseCase
from infrastructure.repositories.task_list import SqlAlchemyTaskListRepository

from uuid import UUID

router = APIRouter(prefix="/task-lists", tags=["Task Lists"])


@router.post("/", response_model=TaskListResponse, status_code=status.HTTP_201_CREATED)
def create_task_list(payload: TaskListCreate):
    repo = SqlAlchemyTaskListRepository()
    usecase = CreateTaskListUseCase(repo)
    task_list = usecase.execute(name=payload.name, description=payload.description)
    return TaskListResponse(**task_list.model_dump())


@router.get("/", response_model=list[TaskListResponse])
def get_all_task_lists():
    repo = SqlAlchemyTaskListRepository()
    task_lists = repo.get_all_task_lists()
    return [TaskListResponse(**tl.model_dump()) for tl in task_lists]


@router.get("/{task_list_id}", response_model=TaskListResponse)
def get_task_list(task_list_id: UUID):
    repo = SqlAlchemyTaskListRepository()
    task_list = repo.get_by_id(task_list_id)
    if not task_list:
        raise HTTPException(status_code=404, detail="Task list not found")
    return TaskListResponse(**task_list.model_dump())


@router.put("/{task_list_id}", response_model=TaskListResponse)
def update_task_list(task_list_id: UUID, payload: TaskListCreate):
    repo = SqlAlchemyTaskListRepository()
    existing = repo.get_by_id(task_list_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Task list not found")

    updated = existing.model_copy(
        update={"name": payload.name, "description": payload.description}
    )

    usecase = UpdateTaskListUseCase(repo)
    result = usecase.execute(updated)
    return TaskListResponse(**result.model_dump())


@router.delete("/{task_list_id}", status_code=204)
def delete_task_list(task_list_id: UUID):
    repo = SqlAlchemyTaskListRepository()
    task_list = repo.get_by_id(task_list_id)
    if not task_list:
        raise HTTPException(status_code=404, detail="Task list not found")

    usecase = DeleteTaskListUseCase(repo)
    usecase.execute(task_list_id)
    return
