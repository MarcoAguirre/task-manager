from usecases.task_list.create import CreateTaskListUseCase
from domain.models.task_list import TaskList
from uuid import UUID
from datetime import datetime
from unittest.mock import MagicMock


def test_create_task_list_returns_valid_task_list():
    fake_repo = MagicMock()
    usecase = CreateTaskListUseCase(fake_repo)

    name = "Mi lista de prueba"
    description = "Descripción de prueba"

    def fake_create(task_list: TaskList) -> TaskList:
        return task_list

    fake_repo.create.side_effect = fake_create

    result = usecase.execute(name=name, description=description)

    assert isinstance(result, TaskList)
    assert result.name == name
    assert result.description == description
    assert isinstance(result.id, UUID)
    assert isinstance(result.created_at, datetime)
