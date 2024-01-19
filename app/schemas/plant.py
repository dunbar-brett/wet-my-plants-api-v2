from typing import Optional
from pydantic import BaseModel, ConfigDict
from pydantic import root_validator


class PlantBase(BaseModel):
    name: str
    species: Optional[str] = None
    user_id: int

    model_config = ConfigDict(extra='allow')

class PlantCreate(BaseModel):
    name: str
    species: Optional[str] = None

class PlantShow(PlantBase):
    id: int
    user_id: int
    is_active: bool
