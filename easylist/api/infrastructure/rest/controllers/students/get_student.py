from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from easylist.api.application.dtos.student_dto import StudentReadDTO
from easylist.api.application.use_cases.student_usecase import StudentUseCase
from easylist.api.infrastructure.rest.controllers.dependencies import get_student_use_case

router = APIRouter()


@router.get("/{student_id}", response_model=StudentReadDTO, status_code=status.HTTP_200_OK)
def get_student(
    student_id: str,
    student_use_case: Annotated[StudentUseCase, Depends(get_student_use_case)],
) -> StudentReadDTO:
    student = student_use_case.get_student(student_id)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student
