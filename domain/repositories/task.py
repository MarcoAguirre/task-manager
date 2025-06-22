from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from domain.models.task import Task

class TaskRepository(ABC):

    @abstractmethod
    def get_by_id(self, task_id: UUID) -> Optional[Task]:
        pass

    @abstractmethod
    def list_by_task_list_id(self, task_list_id: UUID) -> List[Task]:
        pass

    @abstractmethod
    def create(self, task: Task) -> Task:
        pass

    @abstractmethod
    def update(self, task: Task) -> Task:
        pass

    @abstractmethod
    def delete(self, task_id: UUID) -> None:
        pass
