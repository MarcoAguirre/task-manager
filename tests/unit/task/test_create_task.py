from usecases.task.create import CreateTaskUseCase
from domain.models.task import Task, TaskPriority
from uuid import uuid4
from unittest.mock import MagicMock

def test_create_task_creates_valid_task():
    repo = MagicMock()
    repo.create.side_effect = lambda t: t

    usecase = CreateTaskUseCase(repo)
    result = usecase.execute(
        title="Task",
        description="Desc",
        priority=TaskPriority.high,
        task_list_id=uuid4()
    )

    assert isinstance(result, Task)
    assert result.priority == TaskPriority.high
