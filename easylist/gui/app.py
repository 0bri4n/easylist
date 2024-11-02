from gui.components.button import CreateStudentButton
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class GuiApp(QMainWindow):
    """Aplicación principal para gestionar estudiantes."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Gestión de Estudiantes")
        self.setGeometry(100, 100, 300, 200)

        # Configuración de layout principal
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        # Botón de creación de estudiante
        create_button = CreateStudentButton(self)
        layout.addWidget(create_button)
