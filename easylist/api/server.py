from typing import Annotated

from api.application.dtos.student_dto import StudentCreateDTO, StudentReadDTO
from api.application.use_cases.student_usecase import StudentUseCase
from api.domain.repositories.student_repository import StudentRepository
from api.infrastructure.database import Session, get_db
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()


def get_student_use_case(db: Annotated[Session, Depends(get_db)]) -> StudentUseCase:
    return StudentUseCase(StudentRepository(db))


@app.post("/students", response_model=StudentReadDTO, status_code=201)
def create_student(
    student_data: StudentCreateDTO,
    student_use_case: Annotated[StudentUseCase, Depends(get_student_use_case)],
) -> StudentReadDTO:
    try:
        return student_use_case.create_student(student_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


def run_server() -> None:
    import uvicorn

    uvicorn.run(app=app, port=8000)
