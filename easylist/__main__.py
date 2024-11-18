import threading

import uvicorn


def main() -> None:
    server = threading.Thread(
        uvicorn.run("easylist.api.server:app", host="127.0.0.1", port=8000),
        daemon=True,
    )
    server.start()
