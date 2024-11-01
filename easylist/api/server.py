from application.dtos.student_dto import StudentCreateDTO
from application.use_cases.student_usecase import StudentUseCase
from domain.entities.student_entity import Gender
from domain.repositories.student_repository import StudentRepository
from infrastructure.database import SessionLocal


def run_server() -> None:
    student_repository = StudentRepository(SessionLocal())
    student_use_case = StudentUseCase(student_repository)
    student_data = StudentCreateDTO(
        name="Brian Alegre",
        age=20,
        sex=Gender.MALE,
        cedula="001-0000000-0",
        email="brian.alegre@example.com",
    )
    created_student = student_use_case.create_student(student_data)
    print(created_student)


if __name__ == "__main__":
    run_server()
