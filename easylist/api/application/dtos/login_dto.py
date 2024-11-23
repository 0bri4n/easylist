from pydantic import BaseModel, EmailStr, Field, SecretStr


class LoginDTO(BaseModel):
    email: EmailStr = Field(description="User email address", examples=["teacher@example.com"])
    password: SecretStr = Field(description="User password", examples=["Passw0rd!"])


LoginDTO.model_rebuild()
