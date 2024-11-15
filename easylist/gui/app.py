import flet as ft

from .consts import CUSTOM_DARK


def gui_app(page: ft.Page) -> None:
    page.title = "Easylist"

    page.bgcolor = CUSTOM_DARK

    page.add(
        ft.Container(
            content=ft.Text("Hola mundo"),
        ),
    )
    page.update()
