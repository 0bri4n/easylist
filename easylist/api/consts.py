from pathlib import Path
from typing import Final

SECRET_KEY: Final[bytes] = b"MY_SECRET_KEY"

BASE_DIR = Path(__file__).parent.parent
ASSETS_DIR = BASE_DIR.parent / "assets"
STATIC_DIR = BASE_DIR / "api/infrastructure/static"
TEMPLATES_DIR = BASE_DIR / "api/infrastructure/templates"

DATABASE_URL: Final[str] = f"sqlite:///{ASSETS_DIR}/easylist.db"

ASSETS_DIR.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist
