from pydantic import BaseModel, ConfigDict


class TeacherBaseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class TeacherCreateDTO(TeacherBaseDTO): ...


class TeacherReadDTO(TeacherBaseDTO): ...


class TeacherUpdateDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)


TeacherCreateDTO.model_rebuild()
TeacherReadDTO.model_rebuild()
TeacherUpdateDTO.model_rebuild()
