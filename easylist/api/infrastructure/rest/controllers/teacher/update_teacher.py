from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from easylist.api.application.dtos.teacher_dto import TeacherReadDTO, TeacherUpdateDTO
from easylist.api.application.use_cases.teacher_usecase import TeacherUseCase

from .dependencies import get_teacher_use_case

router = APIRouter()


@router.put("/{teacher_id}", response_model=TeacherReadDTO, status_code=status.HTTP_200_OK)
def update_teacher(
    teacher_id: str,
    teacher_data: TeacherUpdateDTO,
    teacher_use_case: Annotated[TeacherUseCase, Depends(get_teacher_use_case)],
) -> TeacherReadDTO:
    updated_teacher = teacher_use_case.update_teacher(teacher_id, teacher_data)
    if not updated_teacher:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
    return updated_teacher
