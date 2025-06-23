from usecases.task.delete import DeleteTaskUseCase
from unittest.mock import MagicMock
from uuid import uuid4

def test_delete_task_calls_repo():
    repo = MagicMock()
    usecase = DeleteTaskUseCase(repo)
    id = uuid4()

    usecase.execute(id)

    repo.delete.assert_called_once_with(id)
