from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from domain.models.task_list import TaskList

class TaskListRepository(ABC):

    @abstractmethod
    def get_by_id(self, task_list_id: UUID) -> Optional[TaskList]:
        pass

    @abstractmethod
    def get_all_task_lists(self) -> List[TaskList]:
        pass

    @abstractmethod
    def create(self, task_list: TaskList) -> TaskList:
        pass

    @abstractmethod
    def update(self, task_list: TaskList) -> TaskList:
        pass

    @abstractmethod
    def delete(self, task_list_id: UUID) -> None:
        pass
