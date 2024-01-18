from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.repos.user import (
    create_user,
    list_users,
    get_user_by_id,
    get_user_by_email,
    update_user,
    delete_user
)
from app.db.session import get_db
from app.schemas.user import UserCreate, UserShow
 
router = APIRouter()
 
 
@router.post("/", response_model=UserShow, status_code=status.HTTP_201_CREATED)
def create(user: UserCreate, db: Session = Depends(get_db)):
    user_with_email = get_user_by_email(email=user.email, db=db)
    if user_with_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    user = create_user(user=user, db=db)
    return user


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    result = delete_user(id=id, db=db)
    if result.get("error"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=result.get("error")
        )
    
    return {"msg": f"Deleted User with id: {id}"}

# TODO remove this later
@router.get("/")
def get_all(db: Session = Depends(get_db)):
    users = list_users(db=db)
    return users


@router.get("/{id}", response_model=UserShow)
def get_by_id(id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(id=id, db=db)
    if user.get("error"):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return user


@router.put("/{id}", response_model=UserShow, status_code=status.HTTP_202_ACCEPTED)
def update(id: int, user: UserCreate, db: Session = Depends(get_db)):
    user = update_user(id=id, user=user, db=db)
    if user.get("error"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=user.get("error")
        )
    
    return user
