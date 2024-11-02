from loguru import logger
from sqlalchemy.exc import SQLAlchemyError

import easylist.api.domain.entities  # noqa: F401 register entities in metadata
from easylist.api.infrastructure.database import Base, engine


def create_tables() -> None:
    try:
        logger.info("Starting table creation in the database...")
        Base.metadata.create_all(bind=engine)
        logger.info("Tables created successfully.")
    except SQLAlchemyError as e:
        logger.error(f"Error creating tables: {e}")
        raise


if __name__ == "__main__":
    create_tables()
