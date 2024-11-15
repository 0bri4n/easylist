from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from easylist.api.application.dtos.student_dto import StudentReadDTO, StudentUpdateDTO
from easylist.api.application.use_cases.student_usecase import StudentUseCase
from easylist.api.infrastructure.rest.controllers.dependencies import get_student_use_case

router = APIRouter()


@router.put("/{student_id}", response_model=StudentReadDTO)
def update_student(
    student_id: str,
    student_data: StudentUpdateDTO,
    student_use_case: Annotated[StudentUseCase, Depends(get_student_use_case)],
) -> StudentReadDTO:
    updated_student = student_use_case.update_student(student_id, student_data)
    if not updated_student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return updated_student
