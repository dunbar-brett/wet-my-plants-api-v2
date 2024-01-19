from fastapi import APIRouter
 
from app.routes.user import router as user_router
from app.routes.plant import router as plant_router
 
 
router = APIRouter(prefix="/api/v1")
 
 
router.include_router(user_router, prefix="/user", tags=["users"])
router.include_router(plant_router, prefix="/plant", tags=["plants"])
 