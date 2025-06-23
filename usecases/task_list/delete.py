from domain.repositories.task_list import TaskListRepository
from uuid import UUID

class DeleteTaskListUseCase:
    def __init__(self, repository: TaskListRepository):
        self.repository = repository

    def execute(self, task_list_id: UUID) -> None:
        self.repository.delete(task_list_id)
