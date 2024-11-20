from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from easylist.api.application.dtos.teacher_dto import TeacherCreateDTO, TeacherReadDTO
from easylist.api.application.use_cases.teacher_usecase import TeacherUseCase

from .dependencies import get_teacher_use_case

router = APIRouter()


@router.post("/", response_model=TeacherReadDTO, status_code=status.HTTP_201_CREATED)
def create_teacher(
    teacher_data: TeacherCreateDTO,
    teacher_use_case: Annotated[TeacherUseCase, Depends(get_teacher_use_case)],
) -> TeacherReadDTO:
    try:
        return teacher_use_case.create_teacher(teacher_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e
    except RuntimeError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) from e
