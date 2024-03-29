import os
from dotenv import load_dotenv


load_dotenv()

class Settings:
    PROJECT_NAME:str = "Wet My Plants"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","127.0.0.1")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432)
    POSTGRES_DB : str = os.getenv("POSTGRES_DB","test_db")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    SUPER_USER_EMAIL: str = os.getenv("WMP_ADMIN_EMAIL")
    SUPER_USER_PASSWORD: str = os.getenv("WMP_ADMIN_PASSWORD")


settings = Settings()