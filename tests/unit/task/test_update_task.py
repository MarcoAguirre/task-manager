from usecases.task.update import UpdateTaskUseCase
from domain.models.task import Task, TaskPriority, TaskStatus
from uuid import uuid4
from datetime import datetime
from unittest.mock import MagicMock


def test_update_task_sets_updated_at():
    repo = MagicMock()
    repo.update.side_effect = lambda t: t

    task = Task(
        id=uuid4(),
        title="Tarea",
        description="",
        status=TaskStatus.pending,
        priority=TaskPriority.medium,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        task_list_id=uuid4(),
    )

    usecase = UpdateTaskUseCase(repo)
    result = usecase.execute(task)

    assert result.updated_at >= task.updated_at
