from domain.repositories.task import TaskRepository
from uuid import UUID


class DeleteTaskUseCase:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def execute(self, task_id: UUID) -> None:
        self.repository.delete(task_id)
