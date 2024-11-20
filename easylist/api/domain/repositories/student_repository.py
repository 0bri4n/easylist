from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from loguru import logger
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from easylist.api.domain.entities.student_entity import StudentEntity
from easylist.api.domain.exceptions import (
    DatabaseError,
    IntegrityConstraintViolationError,
    InvalidUUIDError,
    StudentNotFoundError,
)
from easylist.api.domain.interfaces.intf_student_repo import IStudentRepository
from easylist.api.utils import validate_uuid

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

StudentID = UUID


class StudentRepository(IStudentRepository):
    __slots__ = ("_session",)

    def __init__(self, session: Session) -> None:
        self._session = session

    def create(self, student: StudentEntity) -> StudentEntity:
        try:
            self._session.add(student)
            self._session.commit()
            self._session.refresh(student)
        except IntegrityError as e:
            logger.error(f"Integrity error: {e}")
            self._session.rollback()
            msg = "Duplicate entry for a unique field."
            raise IntegrityConstraintViolationError(msg) from e
        except SQLAlchemyError as e:
            logger.error("Database error during student creation.")
            self._session.rollback()
            msg = "An error occurred while creating the student."
            raise DatabaseError(msg) from e
        return student

    def get_by_id(self, student_id: str) -> StudentEntity | None:
        try:
            uuid_id = validate_uuid(student_id)
            student = self._session.get(StudentEntity, uuid_id)
            if not student:
                msg = f"Student with ID {student_id} does not exist."
                raise StudentNotFoundError(msg)
        except InvalidUUIDError as e:
            logger.warning(f"Invalid UUID format: {student_id}")
            raise e from e
        except SQLAlchemyError as e:
            logger.error(f"Database error during student retrieval: {e}")
            self._session.rollback()
            msg = "An error occurred while retrieving the student."
            raise DatabaseError(msg) from e
        else:
            return student

    def update(self, student_id: str, updated_data: dict) -> StudentEntity:
        student = self.get_by_id(student_id)
        if not student:
            msg = f"Student with ID {student_id} does not exist."
            raise StudentNotFoundError(msg)
        try:
            for key, value in updated_data.items():
                setattr(student, key, value)
            self._session.commit()
            self._session.refresh(student)
        except SQLAlchemyError as e:
            logger.error("Database error during student update.")
            self._session.rollback()
            msg = "An error occurred while updating the student."
            raise DatabaseError(msg) from e
        return student

    def delete(self, student_id: str) -> bool:
        student = self.get_by_id(student_id)
        if not student:
            msg = f"Student with ID {student_id} does not exist."
            raise StudentNotFoundError(msg)
        try:
            self._session.delete(student)
            self._session.commit()
        except SQLAlchemyError as e:
            logger.error("Database error during student deletion.")
            self._session.rollback()
            msg = "An error occurred while deleting the student."
            raise DatabaseError(msg) from e
        else:
            return True
            return True
