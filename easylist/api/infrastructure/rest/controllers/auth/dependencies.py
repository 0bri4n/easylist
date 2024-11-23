from typing import Annotated

from fastapi import Depends

from easylist.api.application.use_cases.auth_usecase import AuthUseCase
from easylist.api.domain.repositories.teacher_repository import TeacherRepository
from easylist.api.infrastructure.database import Session, get_db


def get_auth_use_case(db: Annotated[Session, Depends(get_db)]) -> AuthUseCase:
    return AuthUseCase(teacher_repository=TeacherRepository(db))
