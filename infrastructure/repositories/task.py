from typing import List, Optional
from uuid import UUID

from sqlalchemy.orm import Session

from domain.models.task import Task
from domain.repositories.task import TaskRepository
from infrastructure.db.models import TaskORM
from infrastructure.db.session import SessionLocal
from datetime import datetime


class SqlAlchemyTaskRepository(TaskRepository):
    def __init__(self, session: Optional[Session] = None):
        self.session = session or SessionLocal()

    def get_by_id(self, task_id: UUID) -> Optional[Task]:
        orm_task = (
            self.session.query(TaskORM).filter(TaskORM.id == str(task_id)).first()
        )
        return self._to_domain(orm_task) if orm_task else None

    def list_by_task_list(self, task_list_id: UUID) -> List[Task]:
        orm_task_list = (
            self.session.query(TaskORM)
            .filter(TaskORM.task_list_id == str(task_list_id))
            .all()
        )
        return [self._to_domain(orm) for orm in orm_task_list]

    def create(self, task: Task) -> Task:
        orm_task_obj = TaskORM(
            id=str(task.id),
            title=task.title,
            description=task.description,
            status=task.status,
            priority=task.priority,
            created_at=task.created_at,
            updated_at=task.updated_at,
            task_list_id=str(task.task_list_id),
        )
        self.session.add(orm_task_obj)
        self.session.commit()
        self.session.refresh(orm_task_obj)
        return self._to_domain(orm_task_obj)

    def update(self, task: Task) -> Task:
        orm_task_obj = (
            self.session.query(TaskORM).filter(TaskORM.id == str(task.id)).first()
        )
        if not orm_task_obj:
            raise ValueError("Task not found")
        orm_task_obj.title = task.title
        orm_task_obj.description = task.description
        orm_task_obj.status = task.status
        orm_task_obj.priority = task.priority
        orm_task_obj.updated_at = datetime.now()
        self.session.commit()
        self.session.refresh(orm_task_obj)
        return self._to_domain(orm_task_obj)

    def delete(self, task_id: UUID) -> None:
        orm_task_obj = (
            self.session.query(TaskORM).filter(TaskORM.id == str(task_id)).first()
        )
        if orm_task_obj:
            self.session.delete(orm_task_obj)
            self.session.commit()

    def _to_domain(self, orm: TaskORM) -> Task:
        from uuid import UUID

        return Task(
            id=UUID(orm.id),
            title=orm.title,
            description=orm.description,
            status=orm.status,
            priority=orm.priority,
            created_at=orm.created_at,
            updated_at=orm.updated_at,
            task_list_id=UUID(orm.task_list_id),
        )
