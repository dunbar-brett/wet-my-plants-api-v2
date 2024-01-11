from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.repos.user import create_new_user, list_users
from app.db.session import get_db
from app.schemas.user import UserCreate, UserShow
 
 
router = APIRouter()
 
 
@router.post("/", response_model=UserShow, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user

@router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    users = list_users(db=db)
    return users