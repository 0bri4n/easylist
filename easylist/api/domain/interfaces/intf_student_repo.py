from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from easylist.api.domain.entities.student_entity import StudentEntity


class IStudentRepository(ABC):
    @abstractmethod
    def create(self, student: StudentEntity) -> StudentEntity: ...

    @abstractmethod
    def get_by_id(self, student_id: str) -> StudentEntity | None: ...

    @abstractmethod
    def list_all(self) -> list[StudentEntity]: ...

    @abstractmethod
    def update(self, student_id: str, student_data: dict) -> StudentEntity | None: ...

    @abstractmethod
    def delete(self, student_id: str) -> bool: ...
