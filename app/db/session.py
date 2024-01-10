import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

from app.core.config import Settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SQLALCHEMY_DATABASE_URL = Settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        logger.info("Getting database connection...")
        db = SessionLocal()
        logger.info("Database connection successful!")
        yield db
    finally:
        db.close()