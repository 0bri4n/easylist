from __future__ import annotations

import uuid
from datetime import datetime, timedelta, timezone
from typing import TYPE_CHECKING

import bcrypt
import jwt
from loguru import logger

from easylist.api.consts import JWT_AUDIENCE, SECRET_KEY

if TYPE_CHECKING:
    from easylist.api.application.dtos.login_dto import LoginDTO
    from easylist.api.domain.repositories.teacher_repository import TeacherRepository


class AuthUseCase:
    __slots__ = ("_teacher_repository", "_secret_key", "_token_expiration")

    def __init__(self, teacher_repository: TeacherRepository) -> None:
        self._teacher_repository = teacher_repository
        self._secret_key = SECRET_KEY
        self._token_expiration = timedelta(minutes=60)

    def authenticate(self, login_data: LoginDTO) -> str | None:
        teacher = self._teacher_repository.get_by_email(login_data.email)
        if not teacher:
            logger.warning(f"Authentication failed: No teacher found with email {login_data.email}")
            return None

        if not bcrypt.checkpw(
            login_data.password.get_secret_value().encode("utf-8"),
            teacher.password.encode("utf-8"),
        ):
            logger.warning("Authentication failed: Incorrect password")
            return None

        logger.info(f"Teacher authenticated successfully: {teacher.email}")
        return self._generate_jwt(teacher.id, teacher.email)

    def _generate_jwt(self, teacher_id: str, email: str) -> str:
        payload = {
            "sub": str(teacher_id),
            "aud": JWT_AUDIENCE,  # Restringimos el uso del token a nuestra aplicación
            "iat": datetime.now(timezone.utc),
            "exp": datetime.now(timezone.utc) + self._token_expiration,
            "jti": str(uuid.uuid4()),  # Identificador único del token
        }

        token = jwt.encode(payload, self._secret_key, algorithm="HS256")
        logger.debug(f"Generated JWT for teacher {email}")
        return token
