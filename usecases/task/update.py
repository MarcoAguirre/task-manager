from domain.models.task import Task
from domain.repositories.task import TaskRepository
from datetime import datetime

class UpdateTaskUseCase:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def execute(self, task: Task) -> Task:
        task.updated_at = datetime.utcnow()
        return self.repository.update(task)
