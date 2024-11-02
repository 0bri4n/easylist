import asyncio

from gui.services.api_client import StudentCreateDTO, create_student
from PyQt5.QtWidgets import QMessageBox, QPushButton

from easylist.api.domain.entities.student_entity import Gender


class CreateStudentButton(QPushButton):
    """Botón para enviar datos a la API y crear un estudiante."""

    def __init__(self, parent=None) -> None:
        super().__init__("Crear Estudiante", parent)
        self.clicked.connect(self.on_click)

    def on_click(self) -> None:
        # Datos del estudiante de prueba
        student_data = StudentCreateDTO(
            name="Brian Triste",
            age=20,
            sex=Gender.MALE,
            cedula="055-0000000-0",
            email="dwidnwidnw@example.com",
        )

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.create_student_task(student_data))
        loop.close()

    async def create_student_task(self, student_data) -> None:
        try:
            result = await create_student(student_data)
            QMessageBox.information(self, "Success", f"Estudiante creado con ID: {result['id']}")
        except RuntimeError as error:
            QMessageBox.critical(self, "Error", f"No se pudo crear el estudiante: {error}")
            QMessageBox.information(self, "Success", f"Estudiante creado con ID: {result['id']}")
