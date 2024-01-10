from pydantic import BaseModel

from app.db.models.plant import Plant

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    plants: list[Plant] = []

    class Config:
        orm_mode = True