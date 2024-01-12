from pydantic import BaseModel, ConfigDict

from app.db.models.plant import Plant

class PlantBase(BaseModel):
    name: str
    species: str | None = None

    model_config = ConfigDict(extra='allow')

class PlantCreate(PlantBase):
    pass

class Plant(PlantBase):
    id: int
    user_id: int
    is_active: bool
