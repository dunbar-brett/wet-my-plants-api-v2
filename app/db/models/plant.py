from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.models.base_class import Base


class Plant(Base):
    id = Column(Integer, primary_key=True)
    
    name = Column(String, nullable=False)
    species = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="plants")
    
    # slug = Column(String, nullable=False, unique=True)

    # TODO other fields for later
    # location_id = Column(Integer, ForeignKey("location.id"))
    # location = relationship("Location")
    # fertilizer = Column(String, nullable=True)
    # waterFreq = Column(String, nullable=True) # this should be a enum of some sort
    # imageUrl = Column(String, nullable=True)
    # notes = Column(String, nullable=True)