from uuid import UUID

from easylist.api.domain.exceptions import InvalidUUIDError


def validate_uuid(value: str) -> UUID:
    try:
        return UUID(value, version=4)
    except ValueError as e:
        msg = f"The value '{value}' is not a valid UUID."
        raise InvalidUUIDError(msg) from e
