from __future__ import annotations

from typing import TYPE_CHECKING

from api.application.dtos.student_dto import StudentCreateDTO, StudentReadDTO, StudentUpdateDTO
from api.domain.entities.student_entity import StudentEntity
from loguru import logger

if TYPE_CHECKING:
    from domain.interfaces.intf_student_repo import IStudentRepository


class StudentUseCase:
    __slots__ = ("_student_repository",)

    def __init__(self, student_repository: IStudentRepository) -> None:
        self._student_repository = student_repository

    def create_student(self, student_data: StudentCreateDTO) -> StudentReadDTO:
        student_entity = StudentEntity(**student_data.model_dump())
        created_student = self._student_repository.create(student_entity)
        logger.info(f"Student created with ID: {created_student.id}")
        return StudentReadDTO.model_validate(created_student)

    def get_student(self, student_id: int) -> StudentReadDTO | None:
        student = self._student_repository.get_by_id(student_id)
        return StudentReadDTO.model_validate(student) if student else None

    def update_student(self, student_id: int, student_data: StudentUpdateDTO) -> StudentReadDTO | None:
        updated_student = self._student_repository.update(student_id, student_data.model_dump(exclude_unset=True))
        if updated_student:
            logger.info(f"Student updated with ID: {updated_student.id}")
            return StudentReadDTO.model_validate(updated_student)
        logger.warning(f"Failed to update: Student with ID {student_id} not found")
        return None

    def delete_student(self, student_id: int) -> bool:
        deleted = self._student_repository.delete(student_id)
        if deleted:
            logger.info(f"Student deleted with ID: {student_id}")
        else:
            logger.warning(f"Deletion failed: Student with ID {student_id} not found")
        return deleted
