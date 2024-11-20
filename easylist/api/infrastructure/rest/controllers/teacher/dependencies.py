from typing import Annotated

from fastapi import Depends

from easylist.api.application.use_cases.teacher_usecase import TeacherUseCase
from easylist.api.domain.repositories.teacher_repository import TeacherRepository
from easylist.api.infrastructure.database import Session, get_db


def get_teacher_use_case(db: Annotated[Session, Depends(get_db)]) -> TeacherUseCase:
    return TeacherUseCase(teacher_repository=TeacherRepository(db))
