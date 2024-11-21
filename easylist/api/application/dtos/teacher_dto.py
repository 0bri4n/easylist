from __future__ import annotations

from datetime import datetime
from typing import Annotated
from uuid import UUID  # noqa: TCH003

from pydantic import BaseModel, ConfigDict, EmailStr, Field, SecretStr, StringConstraints


class TeacherBaseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Annotated[
        str,
        StringConstraints(min_length=2, max_length=30),
        Field(description="Teacher full name", examples=["Brian Alegre", "America Perdomo"]),
    ]
    email: Annotated[EmailStr, Field(description="Teacher email address", examples=["teacher@example.com"])]
    profile_image: Annotated[
        str | None,  # No usamos pydantic.HttpUrl por errores que hemos tenido con compatibilidad convirtiendo a str.
        Field(description="URL teacher profile image", examples=["https://example.com/image.jpg"]),
    ]


class TeacherCreateDTO(TeacherBaseDTO):
    password: Annotated[
        SecretStr,
        Field(description="Teacher password", examples=["Passw0rd!", "Secure123"]),
    ]


class TeacherReadDTO(TeacherBaseDTO):
    id: Annotated[UUID, Field(description="Unique identifier for teacher")]
    created_at: Annotated[
        datetime,
        Field(
            alias="createdAt",
            description="Record creation timestamp",
            examples=[datetime.now(tz=datetime.now().astimezone().tzinfo)],
            default_factory=datetime.now,
        ),
    ]


class TeacherUpdateDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Annotated[
        str | None,
        StringConstraints(min_length=2, max_length=30),
        Field(description="Teacher name to update", examples=["Brian Triste", "Europa Perdomo"]),
    ] = None
    email: Annotated[
        EmailStr | None,
        Field(description="Teacher email to update", examples=["updated@example.com"]),
    ] = None
    profile_image: Annotated[
        str | None,
        Field(description="URL teacher profile image to update", examples=["https://example.com/image.jpg"]),
    ] = None
    password: Annotated[
        SecretStr | None,
        Field(description="Teacher password to update", examples=["Passw0rd!", "Secure123"]),
    ] = None


TeacherCreateDTO.model_rebuild()
TeacherReadDTO.model_rebuild()
TeacherUpdateDTO.model_rebuild()
