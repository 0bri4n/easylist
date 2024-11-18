from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm.session import Session

from easylist.api.consts import DATABASE_URL

Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine)

"""Se importa las entidades para que se registren en la metadata de sqlalchemy"""
import easylist.api.domain.entities  # noqa: F401, E402


def get_db() -> Generator[Session]:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
