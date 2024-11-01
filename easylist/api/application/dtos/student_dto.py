from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import datetime

    from domain.entities.student_entity import Gender

from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentBaseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Annotated[str, Field(description="...", examples=["Brian Alegre", "America Perdomo"])]
    age: Annotated[int, Field(description="...", examples=[20])]
    sex: Annotated[Gender | None, Field(description="...", examples=[Gender.MALE, Gender.FEMALE])]
    cedula: Annotated[str, Field(description="...", examples=["001-0000000-0"])]


class StudentCreateDTO(StudentBaseDTO):
    email: Annotated[EmailStr, Field(description="...", examples=["student@example.com"])]


class StudentReadDTO(StudentBaseDTO):
    id: Annotated[int, Field(description="...", examples=[1, 2])]
    created_at: Annotated[
        datetime,
        Field(alias="createdAt", description="...", examples=[datetime.now(tz=datetime.now().astimezone().tzinfo)]),
    ]


class StudentUpdateDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Annotated[
        str | None,
        Field(description="...", examples=["Brian Triste", "Europa Perdomo"]),
    ] = None
    age: Annotated[int | None, Field(description="...", examples=[21])] = None
    sex: Annotated[Gender | None, Field(description="...", examples=["F"])] = None
    cedula: Annotated[str | None, Field(description="...", examples=["002-0000000-0"])] = None
    email: Annotated[EmailStr | None, Field(description="...", examples=["updated@example.com"])] = None
