from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from easylist.api.application.use_cases.student_usecase import StudentUseCase
from easylist.api.infrastructure.rest.controllers.dependencies import get_student_use_case

router = APIRouter()


@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(
    student_id: str,
    student_use_case: Annotated[StudentUseCase, Depends(get_student_use_case)],
) -> None:
    deleted_student = student_use_case.delete_student(student_id)
    if not deleted_student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )
