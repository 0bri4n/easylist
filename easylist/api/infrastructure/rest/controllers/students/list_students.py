from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from easylist.api.application.dtos.student_dto import StudentReadDTO
from easylist.api.application.use_cases.student_usecase import StudentUseCase

from .dependencies import get_student_use_case

router = APIRouter()


@router.get("/list-students", response_model=list[StudentReadDTO], status_code=status.HTTP_200_OK)
def list_students(
    student_use_case: Annotated[StudentUseCase, Depends(get_student_use_case)],
) -> list[StudentReadDTO]:
    students = student_use_case.list_students()

    if not students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No students found.",
        )

    return students
