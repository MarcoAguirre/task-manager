from usecases.task_list.delete import DeleteTaskListUseCase
from unittest.mock import MagicMock
from uuid import uuid4


def test_delete_task_list_calls_repo():
    repo = MagicMock()
    usecase = DeleteTaskListUseCase(repo)
    id = uuid4()

    usecase.execute(id)

    repo.delete.assert_called_once_with(id)
