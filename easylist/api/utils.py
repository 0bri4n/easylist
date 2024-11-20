from uuid import UUID

from easylist.api.domain.exceptions import InvalidUUIDError


def validate_uuid(uuid_str: str) -> UUID:
    try:
        return UUID(uuid_str)
    except ValueError as e:
        msg = f"The provided ID {uuid_str} is not a valid UUID."
        raise InvalidUUIDError(msg) from e
