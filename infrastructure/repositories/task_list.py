from domain.repositories.task_list import TaskListRepository
from domain.models.task_list import TaskList

from infrastructure.db.models import TaskListORM
from infrastructure.db.session import SessionLocal

from sqlalchemy.orm import Session
from uuid import UUID
from typing import Optional, List
from datetime import datetime


class SqlAlchemyTaskListRepository(TaskListRepository):

    def __init__(self, session: Optional[Session] = None):
        self.session = session or SessionLocal()

    def get_by_id(self, task_list_id: UUID) -> Optional[TaskList]:
        orm_task_list = self.session.query(TaskListORM).filter(TaskListORM.id == str(task_list_id)).first()
        return self._to_domain(orm_task_list) if orm_task_list else None

    def get_all_task_lists(self) -> List[TaskList]:
        orm_task_list = self.session.query(TaskListORM).all()
        return [self._to_domain(obj) for obj in orm_task_list]

    def create(self, task_list: TaskList) -> TaskList:
        orm_task_list_obj = TaskListORM(
            id=str(task_list.id),
            name=task_list.name,
            description=task_list.description,
            created_at=task_list.created_at,
            updated_at=task_list.updated_at,
        )
        self.session.add(orm_task_list_obj)
        self.session.commit()
        self.session.refresh(orm_task_list_obj)
        return self._to_domain(orm_task_list_obj)

    def update(self, task_list: TaskList) -> TaskList:
        orm_task_list_obj = self.session.query(TaskListORM).filter(TaskListORM.id == str(task_list.id)).first()
        if not orm_task_list_obj:
            raise ValueError("Task list not found")

        orm_task_list_obj.name = task_list.name
        orm_task_list_obj.description = task_list.description
        orm_task_list_obj.updated_at = datetime.now()

        self.session.commit()
        self.session.refresh(orm_task_list_obj)
        return self._to_domain(orm_task_list_obj)

    def delete(self, task_list_id: UUID) -> None:
        orm_task_list_obj = self.session.query(TaskListORM).filter(TaskListORM.id == str(task_list_id)).first()
        if orm_task_list_obj:
            self.session.delete(orm_task_list_obj)
            self.session.commit()

    def _to_domain(self, task_list_from_orm: TaskListORM) -> TaskList:
        return TaskList(
            id=UUID(task_list_from_orm.id),
            name=task_list_from_orm.name,
            description=task_list_from_orm.description,
            created_at=task_list_from_orm.created_at,
            updated_at=task_list_from_orm.updated_at
        )
