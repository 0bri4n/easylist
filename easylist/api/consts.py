from pathlib import Path
from typing import Final

SECRET_KEY: Final[bytes] = b"MY_SECRET_KEY"  # openssl rand -base64 32
JWT_AUDIENCE: Final[str] = "easylist"

BASE_DIR = Path(__file__).parent.parent
ASSETS_DIR = BASE_DIR.parent / "assets"

DATABASE_URL: Final[str] = f"sqlite:///{ASSETS_DIR}/easylist.db"

ASSETS_DIR.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist
