from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.db.models.plant import Plant

class UserBase(BaseModel):
    email: EmailStr()

    model_config = ConfigDict(extra='allow')


class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=50)

    
class UserShow(UserBase):
    id: int
    is_active: bool


# class User(UserBase):
#     id: int
#     is_active: bool
#     is_superuser: bool
#     plants: list[Plant] = []