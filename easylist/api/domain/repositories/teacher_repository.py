from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from loguru import logger
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from easylist.api.domain.entities.teacher_entity import TeacherEntity
from easylist.api.domain.exceptions import (
    DatabaseError,
    IntegrityConstraintViolationError,
    InvalidUUIDError,
    TeacherNotFoundError,
)
from easylist.api.domain.interfaces.intf_teacher_repo import ITeacherRepository
from easylist.api.utils import validate_uuid

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

TeacherID = UUID


class TeacherRepository(ITeacherRepository):
    __slots__ = ("_session",)

    def __init__(self, session: Session) -> None:
        self._session = session

    def create(self, teacher: TeacherEntity) -> TeacherEntity:
        try:
            self._session.add(teacher)
            self._session.commit()
            self._session.refresh(teacher)
        except IntegrityError as e:
            logger.error(f"Integrity error: {e}")
            self._session.rollback()
            msg = "Duplicate entry for a unique field."
            raise IntegrityConstraintViolationError(msg) from e
        except SQLAlchemyError as e:
            logger.error("Database error during teacher creation.")
            self._session.rollback()
            msg = "An error occurred while creating the teacher."
            raise DatabaseError(msg) from e
        return teacher

    def get_by_id(self, teacher_id: str) -> TeacherEntity | None:
        try:
            uuid_id = validate_uuid(teacher_id)
            teacher = self._session.get(TeacherEntity, uuid_id)
            if not teacher:
                msg = f"Teacher with ID {teacher_id} does not exist."
                raise TeacherNotFoundError(msg)
        except InvalidUUIDError as e:
            logger.warning(f"Invalid UUID format: {teacher_id}")
            raise e from e
        except SQLAlchemyError as e:
            logger.error(f"Database error during teacher retrieval: {e}")
            self._session.rollback()
            msg = "An error occurred while retrieving the teacher."
            raise DatabaseError(msg) from e
        else:
            return teacher

    def get_by_email(self, email: str) -> TeacherEntity | None:
        try:
            teacher = self._session.query(TeacherEntity).filter(TeacherEntity.email == email).one_or_none()
        except SQLAlchemyError as e:
            logger.error(f"Database error during teacher retrieval: {e}")
            self._session.rollback()
            msg = "An error occurred while retrieving the teacher."
            raise DatabaseError(msg) from e
        else:
            return teacher

    def update(self, teacher_id: str, updated_data: dict) -> TeacherEntity:
        teacher = self.get_by_id(teacher_id)
        if not teacher:
            msg = f"Teacher with ID {teacher_id} does not exist."
            raise TeacherNotFoundError(msg)
        try:
            for key, value in updated_data.items():
                setattr(teacher, key, value)
            self._session.commit()
            self._session.refresh(teacher)
        except SQLAlchemyError as e:
            logger.error("Database error during teacher update.")
            self._session.rollback()
            msg = "An error occurred while updating the teacher."
            raise DatabaseError(msg) from e
        return teacher

    def delete(self, teacher_id: str) -> bool:
        teacher = self.get_by_id(teacher_id)
        if not teacher:
            msg = f"Teacher with ID {teacher_id} does not exist."
            raise TeacherNotFoundError(msg)
        try:
            self._session.delete(teacher)
            self._session.commit()
        except SQLAlchemyError as e:
            logger.error("Database error during teacher deletion.")
            self._session.rollback()
            msg = "An error occurred while deleting the teacher."
            raise DatabaseError(msg) from e
        else:
            return True
