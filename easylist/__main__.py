from easylist.api.server import run_server
from easylist.gui.app import GuiApp


async def main() -> None:
    import sys

    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = GuiApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    # todo: impl
    import asyncio
    import threading

    threading.Thread(target=run_server).start()
    asyncio.run(main())
