from usecases.task_list.update import UpdateTaskListUseCase
from domain.models.task_list import TaskList
from unittest.mock import MagicMock
from uuid import uuid4
from datetime import datetime


def test_update_task_list_updates_timestamp():
    repo = MagicMock()
    repo.update.side_effect = lambda tl: tl

    usecase = UpdateTaskListUseCase(repo)

    task_list = TaskList(
        id=uuid4(),
        name="Old Name",
        description="Old",
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

    result = usecase.execute(task_list)

    assert result.name == "Old Name"
    assert result.updated_at >= task_list.updated_at
