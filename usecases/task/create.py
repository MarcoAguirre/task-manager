from uuid import uuid4
from datetime import datetime
from domain.models.task import Task, TaskStatus, TaskPriority
from domain.repositories.task import TaskRepository


class CreateTaskUseCase:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def execute(
        self,
        title: str,
        description: str,
        priority: TaskPriority,
        task_list_id: str,
    ) -> Task:
        task = Task(
            id=uuid4(),
            title=title,
            description=description,
            status=TaskStatus.pending,
            priority=priority,
            task_list_id=task_list_id,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        return self.repository.create(task)
