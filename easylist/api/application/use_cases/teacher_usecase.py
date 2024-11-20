from __future__ import annotations

from typing import TYPE_CHECKING

from loguru import logger

from easylist.api.application.dtos.teacher_dto import TeacherCreateDTO, TeacherReadDTO, TeacherUpdateDTO
from easylist.api.domain.entities.teacher_entity import TeacherEntity

if TYPE_CHECKING:
    from easylist.api.domain.repositories.teacher_repository import TeacherRepository


class TeacherUseCase:
    __slots__ = ("_teacher_repository",)

    def __init__(self, teacher_repository: TeacherRepository) -> None:
        self._teacher_repository = teacher_repository

    def create_teacher(self, teacher_data: TeacherCreateDTO) -> TeacherReadDTO:
        teacher_data.password = teacher_data.password.get_secret_value()

        teacher_entity = TeacherEntity(**teacher_data.model_dump())
        created_teacher = self._teacher_repository.create(teacher_entity)
        logger.info(f"Teacher created with ID: {created_teacher.id}")
        return TeacherReadDTO.model_validate(created_teacher)

    def get_teacher(self, teacher_id: str) -> TeacherReadDTO | None:
        teacher = self._teacher_repository.get_by_id(teacher_id)
        return TeacherReadDTO.model_validate(teacher) if teacher else None

    def update_teacher(self, teacher_id: str, teacher_data: TeacherUpdateDTO) -> TeacherReadDTO | None:
        if teacher_data.password:
            teacher_data.password = teacher_data.password.get_secret_value()

        updated_teacher = self._teacher_repository.update(
            teacher_id,
            teacher_data.model_dump(exclude_unset=True),
        )
        if updated_teacher:
            logger.info(f"Teacher updated with ID: {updated_teacher.id}")
            return TeacherReadDTO.from_orm(updated_teacher)

        logger.warning(f"Failed to update: Teacher with ID {teacher_id} not found")
        return None

    def delete_teacher(self, teacher_id: str) -> bool:
        deleted = self._teacher_repository.delete(teacher_id)
        if deleted:
            logger.info(f"Teacher deleted with ID: {teacher_id}")
        else:
            logger.warning(f"Deletion failed: Teacher with ID {teacher_id} not found")
        return deleted
