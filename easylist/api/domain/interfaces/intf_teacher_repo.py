from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from easylist.api.domain.entities.teacher_entity import TeacherEntity


class ITeacherRepository(ABC):
    @abstractmethod
    def create(self, teacher: TeacherEntity) -> TeacherEntity: ...

    @abstractmethod
    def get_by_id(self, teacher_id: str) -> TeacherEntity | None: ...

    @abstractmethod
    def get_by_email(self, email: str) -> TeacherEntity | None: ...

    @abstractmethod
    def update(self, teacher_id: str, teacher_data: dict) -> TeacherEntity | None: ...

    @abstractmethod
    def delete(self, teacher_id: str) -> bool: ...
