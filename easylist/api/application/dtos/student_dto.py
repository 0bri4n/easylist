from __future__ import annotations

from datetime import datetime  # noqa: TCH003
from typing import Annotated

from api.domain.entities.student_entity import Gender  # noqa: TCH002
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentBaseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Annotated[str, Field(description="Student full name", examples=["Brian Alegre", "America Perdomo"])]
    age: Annotated[int, Field(description="Student age", examples=[20])]
    sex: Annotated[Gender | None, Field(description="Student's gender", examples=[Gender.MALE, Gender.FEMALE])]
    cedula: Annotated[str, Field(description="Student's ID number", examples=["001-0000000-0"])]


class StudentCreateDTO(StudentBaseDTO):
    email: Annotated[EmailStr, Field(description="Student's email address", examples=["student@example.com"])]


class StudentReadDTO(StudentBaseDTO):
    id: Annotated[int, Field(description="Unique identifier for student", examples=[1, 2])]
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
        Field(description="Student name to update", examples=["Brian Triste", "Europa Perdomo"]),
    ] = None
    age: Annotated[int | None, Field(description="Age to update", examples=[21])] = None
    sex: Annotated[Gender | None, Field(description="Gender to update", examples=[Gender.MALE, Gender.FEMALE])] = None
    cedula: Annotated[str | None, Field(description="Updated ID number", examples=["002-0000000-0"])] = None
    email: Annotated[EmailStr | None, Field(description="Updated email address", examples=["updated@example.com"])] = (
        None
    )


StudentCreateDTO.model_rebuild()
StudentReadDTO.model_rebuild()
StudentUpdateDTO.model_rebuild()
