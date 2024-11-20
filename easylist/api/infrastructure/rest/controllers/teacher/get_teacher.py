from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from easylist.api.application.dtos.teacher_dto import TeacherReadDTO
from easylist.api.application.use_cases.teacher_usecase import TeacherUseCase

from .dependencies import get_teacher_use_case

router = APIRouter()


@router.get("/{teacher_id}", response_model=TeacherReadDTO, status_code=status.HTTP_200_OK)
def get_teacher(
    teacher_id: str,
    teacher_use_case: Annotated[TeacherUseCase, Depends(get_teacher_use_case)],
) -> TeacherReadDTO:
    teacher = teacher_use_case.get_teacher(teacher_id)
    if not teacher:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
    return teacher
