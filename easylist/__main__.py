import threading

import flet as ft
import uvicorn

from .gui.app import gui_app


def start_server() -> None:
    uvicorn.run(
        "easylist.api.server:app",
        host="127.0.0.1",
        port=8000,
        log_level="info",
    )


def main() -> None:
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    ft.app(gui_app)
