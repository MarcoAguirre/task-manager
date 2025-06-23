from usecases.task_list.read import (
    GetFilteredTasksWithProgressUseCase,
    FilteredTasksWithProgressResult
)
from domain.models.task import Task, TaskStatus, TaskPriority
from uuid import uuid4
from datetime import datetime
from unittest.mock import MagicMock

def test_filtered_tasks_with_progress_returns_filtered_tasks_and_percentage():
    repo = MagicMock()
    task_list_id = uuid4()

    tasks = [
        Task(id=uuid4(), title="1", description="", status=TaskStatus.completed, priority=TaskPriority.low, created_at=datetime.now(), updated_at=datetime.now(), task_list_id=task_list_id),
        Task(id=uuid4(), title="2", description="", status=TaskStatus.pending, priority=TaskPriority.low, created_at=datetime.now(), updated_at=datetime.now(), task_list_id=task_list_id),
    ]

    repo.list_by_task_list.return_value = tasks
    usecase = GetFilteredTasksWithProgressUseCase(repo)

    result = usecase.execute(task_list_id=task_list_id, status=TaskStatus.completed)

    assert isinstance(result, FilteredTasksWithProgressResult)
    assert len(result.tasks) == 1
    assert result.completion_percentage == 50
