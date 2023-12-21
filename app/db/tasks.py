from fastapi import FastAPI
from databases import Database
from app.core.config import DATABASE_URL
import logging
 
logger = logging.getLogger(__name__)
 
 
async def connect_to_db(app: FastAPI) -> None:
    logger.info(f"--- DB URL {DATABASE_URL} ---")
    database = Database(DATABASE_URL, min_size=2, max_size=10)  # these can be configured in config as well
    logger.info("--- DB CONNECTING ---")
    try:
        await database.connect()
        app.state._db = database
        logger.info("--- DB CONNECTED ---")
    except Exception as e:
        logger.warn("--- DB CONNECTION ERROR ---")
        logger.warn(e)
        logger.warn("--- DB CONNECTION ERROR ---")
 
 
async def close_db_connection(app: FastAPI) -> None:
    logger.info("--- DB DISCONNECTING ---")
    try:
        await app.state._db.disconnect()
    except Exception as e:
        logger.warn("--- DB DISCONNECT ERROR ---")
        logger.warn(e)
        logger.warn("--- DB DISCONNECT ERROR ---")
 