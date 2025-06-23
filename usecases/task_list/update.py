from domain.models.task_list import TaskList
from domain.repositories.task_list import TaskListRepository
from datetime import datetime


class UpdateTaskListUseCase:
    def __init__(self, repository: TaskListRepository):
        self.repository = repository

    def execute(self, task_list: TaskList) -> TaskList:
        task_list.updated_at = datetime.utcnow()
        return self.repository.update(task_list)
