from pydantic import BaseModel

from app.db.models.plant import Plant

class PlantBase(BaseModel):
    name: str
    species: str | None = None

class PlantCreate(PlantBase):
    pass

class Plant(PlantBase):
    id: int
    user_id: int
    is_active: bool

    class Config:
        orm_mode = True