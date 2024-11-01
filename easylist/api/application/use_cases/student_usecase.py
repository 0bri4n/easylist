from __future__ import annotations

from typing import TYPE_CHECKING

from application.dtos.student_dto import StudentCreateDTO, StudentReadDTO, StudentUpdateDTO
from domain.entities.student_entity import StudentEntity

if TYPE_CHECKING:
    from domain.interfaces.intf_student_repo import IStudentRepository


class StudentUseCase:
    __slots__ = ("_student_repository",)

    def __init__(self, student_repository: IStudentRepository) -> None:
        self._student_repository = student_repository

    def create_student(self, student_data: StudentCreateDTO) -> StudentReadDTO:
        student_entity = StudentEntity(**student_data.model_dump())
        created_student = self._student_repository.create(student_entity)
        return StudentReadDTO.model_validate(created_student)

    def get_student(self, student_id: int) -> StudentReadDTO | None:
        student = self._student_repository.get_by_id(student_id)
        return StudentReadDTO.model_validate(student) if student else None

    def update_student(self, student_id: int, student_data: StudentUpdateDTO) -> StudentReadDTO | None:
        updated_student = self._student_repository.update(student_id, student_data.model_dump(exclude_unset=True))
        return StudentReadDTO.model_validate(updated_student) if updated_student else None

    def delete_student(self, student_id: int) -> bool:
        return self._student_repository.delete(student_id)
