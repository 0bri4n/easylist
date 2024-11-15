from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from easylist.api.application.dtos.student_dto import StudentCreateDTO, StudentReadDTO
from easylist.api.application.use_cases.student_usecase import StudentUseCase
from easylist.api.infrastructure.rest.controllers.dependencies import get_student_use_case

router = APIRouter()


@router.post("/", response_model=StudentReadDTO, status_code=status.HTTP_201_CREATED)
def create_student(
    student_data: StudentCreateDTO,
    student_use_case: Annotated[StudentUseCase, Depends(get_student_use_case)],
) -> StudentReadDTO:
    try:
        return student_use_case.create_student(student_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e
    except RuntimeError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)) from e
