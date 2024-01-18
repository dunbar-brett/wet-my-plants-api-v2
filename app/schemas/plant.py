from pydantic import BaseModel, ConfigDict

from app.db.models.plant import Plant

class PlantBase(BaseModel):
    name: str
    species: str | None = None
    user_id: int

    model_config = ConfigDict(extra='allow')

class PlantCreate(PlantBase):
    pass

class PlantShow(PlantBase):
    id: int
    user_id: int
    is_active: bool
