from pathlib import Path

ASSETS_DIR = Path(__file__).parent.parent.parent / "assets"
DATABASE_URL = f"sqlite:///{ASSETS_DIR}/easylist.db"

ASSETS_DIR.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist
