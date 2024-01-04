from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router as api_router
from app.core import config, tasks  

 
def get_application():
    app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)  

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_event_handler("startup", tasks.create_start_app_handler(app))
    app.add_event_handler("shutdown", tasks.create_stop_app_handler(app))

    app.include_router(api_router, prefix="/api")

    return app

app = get_application()
 

# # main.py
# from fastapi import FastAPI, Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, relationship
# from databases import Database
# from jose import JWTError, jwt
# from passlib.context import CryptContext

# DATABASE_URL = "sqlite:///./test.db"

# SECRET_KEY = "your-secret-key"
# ALGORITHM = "HS256"

# Base = declarative_base()

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# database = Database(DATABASE_URL)

# app = FastAPI()

# # Security
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# # Models
# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     plants = relationship("Plant", back_populates="owner")


# class Plant(Base):
#     __tablename__ = "plants"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     species = Column(String)
#     description = Column(String)
#     notes = Column(String)
#     water_frequency = Column(Integer)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     location_id = Column(Integer, ForeignKey("locations.id"))
#     owner = relationship("User", back_populates="plants")


# class Location(Base):
#     __tablename__ = "locations"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     plants = relationship("Plant", back_populates="location")


# Base.metadata.create_all(bind=engine)


# # Dependency to get the current user from the token
# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Invalid credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = {"sub": username}
#     except JWTError:
#         raise credentials_exception
#     return token_data


# # Dependency to get the database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# # Routes
# @app.post("/token")
# async def login_for_access_token(form_data: OAuth2PasswordBearer = Depends()):
#     db = SessionLocal()
#     user = db.query(User).filter(User.email == form_data.username).first()
#     if not user or not pwd_context.verify(form_data.password, user.hashed_password):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect email or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     token_data = {"sub": user.email}
#     token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
#     return {"access_token": token, "token_type": "bearer"}


# @app.get("/users/me", response_model=User)
# async def read_users_me(current_user: User = Depends(get_current_user)):
#     return current_user


# @app.post("/users/", response_model=User)
# async def create_user(user: User, db: SessionLocal = Depends(get_db)):
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user


# @app.get("/plants/{plant_id}", response_model=Plant)
# async def read_plant(plant_id: int, db: SessionLocal = Depends(get_db)):
#     plant = db.query(Plant).filter(Plant.id == plant_id).first()
#     if plant is None:
#         raise HTTPException(status_code=404, detail="Plant not found")
#     return plant


# @app.post("/plants/", response_model=Plant)
# async def create_plant(plant: Plant, db: SessionLocal = Depends(get_db), current_user: User = Depends(get_current_user)):
#     plant.user_id = current_user["sub"]
#     db.add(plant)
#     db.commit()
#     db.refresh(plant)
#     return plant


# @app.post("/locations/", response_model=Location)
# async def create_location(location: Location, db: SessionLocal = Depends(get_db), current_user: User = Depends(get_current_user)):
#     location.user_id = current_user["sub"]
#     db.add(location)
#     db.commit()
#     db.refresh(location)
#     return location