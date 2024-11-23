from __future__ import annotations

import uuid
from datetime import datetime  # noqa: TCH003
from typing import TYPE_CHECKING, Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field, StringConstraints

from easylist.api.domain.entities.student_entity import Gender  # noqa: TCH001

if TYPE_CHECKING:
    from re import Pattern


CEDULA_REGEX: Pattern[str] = r"^\d{3}-\d{7}-\d{1}$"


class StudentBaseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Annotated[
        str | None,
        StringConstraints(min_length=2, max_length=30),
        Field(description="Student full name", examples=["Brian Alegre", "America Perdomo"]),
    ]
    age: Annotated[int, Field(ge=8, le=100, description="Student age", examples=[20])]
    sex: Annotated[Gender, Field(description="Student's gender", examples=[Gender.MALE, Gender.FEMALE])]
    cedula: Annotated[
        str | None,
        StringConstraints(pattern=CEDULA_REGEX),
        Field(description="Student's ID number", examples=["001-0000000-0"]),
    ] = None


class StudentCreateDTO(StudentBaseDTO):
    email: Annotated[EmailStr, Field(description="Student's email address", examples=["student@example.com"])]


class StudentReadDTO(StudentBaseDTO):
    id: Annotated[UUID, Field(default=uuid.uuid4, description="Student unique identifier")]
    created_at: Annotated[
        datetime,
        Field(
            alias="createdAt",
            description="Record creation timestamp",
            examples=[datetime.now(tz=datetime.now().astimezone().tzinfo)],
            default_factory=datetime.now,
        ),
    ]


class StudentUpdateDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Annotated[
        str | None,
        StringConstraints(min_length=2, max_length=30),
        Field(description="Student name to update", examples=["Brian Triste", "Europa Perdomo"]),
    ] = None
    age: Annotated[int | None, Field(ge=8, le=100, description="Age to update", examples=[21])] = None
    sex: Annotated[Gender | None, Field(description="Gender to update", examples=[Gender.MALE, Gender.FEMALE])] = None
    cedula: Annotated[
        str | None,
        StringConstraints(pattern=CEDULA_REGEX),
        Field(description="Updated ID number", examples=["002-0000000-0"]),
    ] = None
    email: Annotated[
        EmailStr | None,
        Field(description="Updated email address", examples=["updated@example.com"]),
    ] = None


StudentCreateDTO.model_rebuild()
StudentReadDTO.model_rebuild()
StudentUpdateDTO.model_rebuild()
