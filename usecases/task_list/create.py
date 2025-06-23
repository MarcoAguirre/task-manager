from domain.models.task_list import TaskList
from domain.repositories.task_list import TaskListRepository
from uuid import uuid4
from datetime import datetime


class CreateTaskListUseCase:
    def __init__(self, repository: TaskListRepository):
        self.repository = repository

    def execute(self, name: str, description: str = "") -> TaskList:
        task_list = TaskList(
            id=uuid4(),
            name=name,
            description=description,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        return self.repository.create(task_list)
