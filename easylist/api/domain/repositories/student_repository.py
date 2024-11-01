from __future__ import annotations

from typing import TYPE_CHECKING

from domain.entities.student_entity import StudentEntity
from domain.interfaces.intf_student_repo import IStudentRepository
from loguru import logger
from sqlalchemy.exc import SQLAlchemyError

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


class StudentRepository(IStudentRepository):
    __slots__ = ("_session",)

    def __init__(self, session: Session) -> None:
        self._session = session

    def create(self, student: StudentEntity) -> StudentEntity:
        try:
            self._session.add(student)
            self._session.commit()
            self._session.refresh(student)
            logger.info("Student created with ID: %s", student.id)
        except SQLAlchemyError:
            self._session.rollback()
            logger.exception("Error creating student with data: %s", student)
            raise
        else:
            return student

    def get_by_id(self, student_id: int) -> StudentEntity | None:
        return self._session.query(StudentEntity).filter_by(id=student_id).first()

    def list_all(self) -> list[StudentEntity]:
        return self._session.query(StudentEntity).all()

    def update(self, student_id: int, student_data: dict) -> StudentEntity | None:
        student = self.get_by_id(student_id)

        if student:
            try:
                for key, value in student_data.items():
                    setattr(student, key, value)
                self._session.commit()
                self._session.refresh(student)
                logger.info("Student updated with ID: %s", student.id)
            except SQLAlchemyError:
                self._session.rollback()
                logger.exception("Error updating student with ID %s: %s", student_id, student_data)
                raise
            else:
                return student
        return None

    def delete(self, student_id: int) -> bool:
        student = self.get_by_id(student_id)

        if student:
            try:
                self._session.delete(student)
                self._session.commit()
                logger.info("Student deleted with ID: %s", student_id)
            except SQLAlchemyError:
                self._session.rollback()
                logger.exception("Error deleting student with ID: %s", student_id)
                raise
            else:
                return True
        return False
