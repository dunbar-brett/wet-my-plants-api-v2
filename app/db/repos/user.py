from sqlalchemy.orm import Session

from app.core.hasher import Hasher
from app.db.models.user import User
from app.schemas.user import UserCreate


def create_new_user(user: UserCreate, db: Session):
    db_user = User(
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def list_users(db: Session):
    users = db.query(User).filter(User.is_active == True).all()
    return users