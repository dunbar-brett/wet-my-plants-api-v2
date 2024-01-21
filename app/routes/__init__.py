from fastapi import APIRouter
 
from app.routes.login import router as login_router
from app.routes.plant import router as plant_router
from app.routes.user import router as user_router
 
 
router = APIRouter(prefix="/api/v1")
 
router.include_router(login_router, prefix="", tags=["login"])
router.include_router(plant_router, prefix="/plant", tags=["plants"])
router.include_router(user_router, prefix="/user", tags=["users"])
 