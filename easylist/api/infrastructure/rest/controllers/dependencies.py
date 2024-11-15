from typing import Annotated

from fastapi import Depends

from easylist.api.application.use_cases.student_usecase import StudentUseCase
from easylist.api.domain.repositories.student_repository import StudentRepository
from easylist.api.infrastructure.database import Session, get_db


def get_student_use_case(db: Annotated[Session, Depends(get_db)]) -> StudentUseCase:
    return StudentUseCase(StudentRepository(db))
