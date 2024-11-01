from datetime import datetime
from enum import Enum

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy import Enum as SQLAlchemyEnum

from easylist.api.infrastructure.database import Base


class Gender(str, Enum):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"


class StudentEntity(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, index=True)
    age = Column(Integer, nullable=False)
    sex = Column(SQLAlchemyEnum(Gender), nullable=False)
    cedula = Column(String(15), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return (
            f"<StudentEntity(id={self.id}, name={self.name}, age={self.age}, sex={self.sex}, "
            f"cedula={self.cedula}, email={self.email}, created_at={self.created_at})>"
        )
