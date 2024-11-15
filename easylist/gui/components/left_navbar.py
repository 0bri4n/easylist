import flet as ft

from easylist.gui.consts import CUSTOM_DARK


def appbar() -> None:
    return ft.AppBar(
        bgcolor=CUSTOM_DARK,
        actions=[
            ft.Container(
                ft.Text("Easy list"),
            ),
        ],
    )


class LeftNavbar(ft.UserControl):
    def __init__(self) -> None:
        super().__init__()

    def data(self, initials) -> None:
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        width=42,
                        height=42,
                        bgcolor="bluegray900",
                        alignment=ft.alignment.center,
                        border_radius=8,
                        content=ft.Text(initials, size=20, weight="bold"),
                    ),
                ],
            ),
        )

    def build(self) -> None:
        return ft.Container(
            width=200,
            height=580,
            padding=ft.padding.only(top=10),
            alignment=ft.alignment.center,
            content=ft.Column(controls=[self.data("LI")]),
        )
