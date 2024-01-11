from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.models.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_superuser = Column(Boolean(), default=False)
    plants = relationship("Plant", back_populates="user")
    # locations = relationship("Location", back_populates="user")