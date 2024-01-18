from sqlalchemy.orm import Session

from app.db.models.plant import Plant
from app.schemas.plant import PlantCreate


def create_plant(plant: PlantCreate, user_id: int, db: Session):
    db_plant = Plant(
        name=plant.name,
        species=plant.species,
        user_id=user_id,
        is_active=True
    )
    db.add(db_plant)
    db.commit()
    db.refresh(db_plant)
    return db_plant


def deactivate_plant(id: int, db: Session):
    plant = get_plant_by_id(id=id, db=db)
    if not plant:
        return plant
    
    plant.is_active = False
    db.commit()
    return plant

def delete_plant(id: int, db: Session):
    plant = get_plant_by_id(id=id, db=db)
    if not plant:
        return plant
    
    db.delete(plant)
    db.commit()
    return plant


def get_plant_by_id(id: int, db: Session):
    plant = db.query(Plant).filter(Plant.id == id).first()
    return plant

# TODO: remove this later
def list_plants(db: Session):
    plants = db.query(Plant).filter(Plant.is_active == True).all()
    return plants


def update_plant(id: int, plant: PlantCreate, db: Session):
    db_plant = get_plant_by_id(id=id, db=db)
    if not db_plant:
        return db_plant
    
    db_plant.name = plant.name
    db_plant.species = plant.species
    db.commit()
    db.refresh(db_plant)
    return db_plant