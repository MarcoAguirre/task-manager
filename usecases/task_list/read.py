from typing import List, Optional
from uuid import UUID
from domain.models.task import Task, TaskStatus, TaskPriority
from domain.repositories.task import TaskRepository


class FilteredTasksWithProgressResult:
    def __init__(self, tasks: List[Task], completion_percentage: int):
        self.tasks = tasks
        self.completion_percentage = completion_percentage


class GetFilteredTasksWithProgressUseCase:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def execute(
        self,
        task_list_id: UUID,
        status: Optional[TaskStatus] = None,
        priority: Optional[TaskPriority] = None,
    ) -> FilteredTasksWithProgressResult:
        all_tasks = self.repository.list_by_task_list(task_list_id)

        filtered = [
            task
            for task in all_tasks
            if (not status or task.status == status)
            and (not priority or task.priority == priority)
        ]

        total = len(all_tasks)
        completed = len(
            [task for task in all_tasks if task.status == TaskStatus.completed]
        )
        percentage = int((completed / total) * 100) if total > 0 else 0

        return FilteredTasksWithProgressResult(
            tasks=filtered, completion_percentage=percentage
        )
