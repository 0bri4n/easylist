from __future__ import annotations

from typing import Final

from argon2 import PasswordHasher
from argon2.exceptions import HashingError, InvalidHash, VerificationError, VerifyMismatchError, VerifyUnusualError
from loguru import logger

DEFAULT_TIME_COST: Final[int] = 3
DEFAULT_MEMORY_COST: Final[int] = 64**1024  # 64 MB
DEFAULT_PARALLELISM: Final[int] = 4


class HashService:
    __slots__ = ("_hasher",)

    def __init__(
        self,
        time_cost: int = DEFAULT_TIME_COST,
        memory_cost: int = DEFAULT_MEMORY_COST,
        parallelism: int = DEFAULT_PARALLELISM,
    ) -> None:
        self._hasher: Final[PasswordHasher] = PasswordHasher(
            time_cost,
            memory_cost,
            parallelism,
        )

    def hash_password(self, password: str) -> str | None:
        try:
            return self._hasher.hash(password)
        except HashingError as e:
            logger.error(f"Error hashing password: {e}")

    def verify_password(self, password: str, hash_: str) -> bool:
        try:
            return self._hasher.verify(hash_, password)
        except VerifyMismatchError:
            return False
        except (VerifyUnusualError, VerificationError, InvalidHash) as e:
            logger.error(f"Error verifying password: {e}")
            return False
