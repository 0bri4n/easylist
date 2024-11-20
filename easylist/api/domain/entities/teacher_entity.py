import uuid
from datetime import datetime
from typing import ClassVar

from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID

from easylist.api.infrastructure.database import Base


class TeacherEntity(Base):
    __tablename__ = "teacher"
    __table_args__: ClassVar = {"extend_existing": True}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String(100), nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    profile_image = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return (
            f"<TeacherEntity(id={self.id}, name={self.name}, email={self.email}, "
            f"profile_image={self.profile_image}, created_at={self.created_at})>"
        )
