from __future__ import annotations

from typing import TYPE_CHECKING

from domain.entities.student_entity import StudentEntity
from domain.interfaces.intf_student_repo import IStudentRepository
from loguru import logger
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError

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
            logger.info(f"Student created with ID: {student.id}")
        except IntegrityError as e:
            self._session.rollback()
            logger.error(f"Integrity error: Duplicate entry detected for student data: {student}")
            msg = "Student with the provided unique attributes already exists."
            raise ValueError(msg) from e
        except (SQLAlchemyError, OperationalError) as e:
            self._session.rollback()
            logger.exception(f"Error creating student with data: {student}")
            msg = f"Failed to create student: {e}"
            raise RuntimeError(msg) from e
        return student

    def get_by_id(self, student_id: int) -> StudentEntity | None:
        return self._session.query(StudentEntity).filter_by(id=student_id).first()

    def list_all(self) -> list[StudentEntity]:
        students = self._session.query(StudentEntity).all()
        if not students:
            logger.warning("No students found in the database")
        return students

    def update(self, student_id: int, student_data: dict) -> StudentEntity | None:
        student = self.get_by_id(student_id)
        if student:
            try:
                for key, value in student_data.items():
                    setattr(student, key, value)
                self._session.commit()
                self._session.refresh(student)
                logger.info(f"Student updated with ID: {student.id}")
            except IntegrityError as e:
                self._session.rollback()
                logger.error(f"Integrity error: Duplicate entry detected for student data: {student_data}")
                msg = "Update failed: Duplicate unique attributes found."
                raise ValueError(msg) from e
            except (SQLAlchemyError, OperationalError) as e:
                self._session.rollback()
                logger.exception(f"Error updating student with ID {student_id}: {student_data}")
                msg = f"Failed to update student: {e}"
                raise RuntimeError(msg) from e
            return student
        logger.warning(f"Student with ID {student_id} not found for update")
        return None

    def delete(self, student_id: int) -> bool:
        student = self.get_by_id(student_id)
        if student:
            try:
                self._session.delete(student)
                self._session.commit()
                logger.info(f"Student deleted with ID: {student_id}")
            except (SQLAlchemyError, OperationalError) as e:
                self._session.rollback()
                logger.exception(f"Error deleting student with ID: {student_id}")
                msg = f"Failed to delete student: {e}"
                raise RuntimeError(msg) from e
            return True
        logger.warning(f"Student with ID {student_id} not found for deletion")
        return False
