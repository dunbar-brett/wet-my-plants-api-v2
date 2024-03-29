from sqlalchemy.orm import Session

from app.core.hasher import Hasher
from app.db.models.user import User
from app.schemas.user import UserCreate


def create_user(user: UserCreate, db: Session):
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


def deactivate_user(id: int, db: Session):
    user = get_user_by_id(id=id, db=db)
    if not user:
        return user
    
    user.is_active = False
    db.commit()
    return user


def delete_user(id: int, db: Session):
    user = get_user_by_id(id=id, db=db)
    if not user:
        return None
    
    db.delete(user)
    db.commit()
    return user


def get_user(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user


def get_user_by_id(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        return None
    
    return user


# TODO: remove this later
def list_users(db: Session):
    users = db.query(User).filter(User.is_active == True).all()
    return users


def update_user(id: int, user: UserCreate, db: Session):
    user_email_check = db.query(User).filter(User.email == user.email).first()
    if user_email_check:
        return {"error": f"User with email {user.email} already exists"}
    
    db_user = db.query(User).filter(User.id == id).first()
    db_user.email = user.email
    db_user.hashed_password = Hasher.get_password_hash(user.password)
    db.commit()
    db.refresh(user)
    return user
