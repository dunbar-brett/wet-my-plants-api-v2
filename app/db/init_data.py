import logging
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import Settings
from app.core.hasher import Hasher
from app.db.models.user import User

# logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_super_user(session: Session) -> None:
    super_user = session.scalars(
        select(User).where(User.email == Settings.SUPER_USER_EMAIL)
    ).first()

    if not super_user:
        logger.info("Creating super user...")
        super_user = User(
            email=Settings.SUPER_USER_EMAIL,
            hashed_password=Hasher.get_password_hash(Settings.SUPER_USER_PASSWORD),
            is_active=True,
            is_superuser=True
        )
        session.add(super_user)
        session.commit()
        session.refresh(super_user)

    return super_user
