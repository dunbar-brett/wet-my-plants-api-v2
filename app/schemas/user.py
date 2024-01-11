from pydantic import BaseModel, EmailStr

from app.db.models.plant import Plant

class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


# class User(UserBase):
#     id: int
#     is_active: bool
#     is_superuser: bool
#     plants: list[Plant] = []

#     class Config:
#         orm_mode = True
    
class UserShow(UserBase):
    id: int
    is_superuser: bool
    is_active: bool

    class Config:  # tells pydantic to convert even non dict obj to json
        orm_mode = True