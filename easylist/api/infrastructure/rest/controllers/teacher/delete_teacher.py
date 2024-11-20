from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from easylist.api.application.use_cases.teacher_usecase import TeacherUseCase

from .dependencies import get_teacher_use_case

router = APIRouter()


@router.delete("/{teacher_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_teacher(
    teacher_id: str,
    teacher_use_case: Annotated[TeacherUseCase, Depends(get_teacher_use_case)],
) -> None:
    deleted_teacher = teacher_use_case.delete_teacher(teacher_id)
    if not deleted_teacher:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher not found",
        )
