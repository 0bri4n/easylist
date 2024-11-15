from sqlalchemy import MetaData

from .student_entity import StudentEntity

Metadata = MetaData()

__all__ = ("StudentEntity",)
