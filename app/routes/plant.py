from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.models.user import User
from app.db.repos.plant import create_plant, delete_plant, get_plant_by_id, list_plants, list_plants_by_user, update_plant

from app.db.session import get_db
from app.routes.login import get_current_user
from app.schemas.plant import PlantCreate, PlantShow

router = APIRouter()


@router.post("/", response_model=PlantShow, status_code=status.HTTP_201_CREATED)
def create(plant: PlantCreate, db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)):
    db_plant = create_plant(plant=plant, user_id=current_user.id, db=db)

    return db_plant


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    plant = delete_plant(id=id, db=db)
    if not plant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Plant not found"
        )
    
    return {"msg": f"Deleted Plant with id: {id}"}


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    plants = list_plants(db=db)
    return plants

@router.get("/{user_id}")
def get_all_by_user(user_id: int, db: Session = Depends(get_db)):
    plants = list_plants_by_user(user_id=user_id, db=db)
    return plants


@router.get("/{id}", response_model=PlantShow)
def get_by_id(id: int, db: Session = Depends(get_db)):
    plant = get_plant_by_id(id=id, db=db)
    if not plant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Plant not found"
        )
    
    return plant


@router.put("/{id}", response_model=PlantShow, status_code=status.HTTP_202_ACCEPTED)
def update(id: int, plant: PlantCreate, db: Session = Depends(get_db)):
    db_plant = update_plant(id=id, plant=plant, db=db)
    if not db_plant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Plant not found"
        )

    return db_plant