import logging

from app.db.session import get_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_db():
    logger.info("Testing database connection...")
    get_db()
    logger.info("Database connection successful!")