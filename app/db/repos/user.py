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

# TODO: remove this later
def list_users(db: Session):
    users = db.query(User).filter(User.is_active == True).all()
    return users

def get_user_by_id(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        return {"error": f"User with id {id} not found"}
    return user

def get_user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return {"error": f"User with email {email} not found"}
    return user

def update_user(id: int, user: UserCreate, db: Session):
    user_email_check = db.query(User).filter(User.email == user.email).first()
    if user_email_check:
        return {"error": f"User with email {user.email} already exists"}

    user = db.query(User).filter(User.id == id).first()
    user.email = user.email
    user.hashed_password = Hasher.get_password_hash(user.password)
    db.commit()
    db.refresh(user)
    return user

def delete_user(id: int, db: Session):
    user = get_user_by_id(id=id, db=db)
    if user.get("error"):
        return user
    db.delete(user)
    db.commit()
    return user

def deactivate_user(id: int, db: Session):
    user = get_user_by_id(id=id, db=db)
    if user.get("error"):
        return user
    user.is_active = False
    db.commit()
    return user