class StudentNotFoundError(Exception):
    """Raised when a student is not found in the database."""


class TeacherNotFoundError(Exception):
    """Raised when a teacher is not found in the database."""


class InvalidUUIDError(ValueError):
    """Raised when an invalid UUID format is provided."""


class DatabaseError(Exception):
    """Raised for general database errors."""


class IntegrityConstraintViolationError(ValueError):
    """Raised when an integrity constraint (e.g., unique) is violated."""
