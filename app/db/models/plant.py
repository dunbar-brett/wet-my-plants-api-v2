from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.models.base import Base


class Plant(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    slug = Column(String, nullable=False, unique=True) # TODO: do i need this?
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="plants")
    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=False)

    # TODO other fields for later
    # species = Column(String, nullable=True)
    # location_id = Column(Integer, ForeignKey("location.id"))
    # location = relationship("Location")
    # fertilizer = Column(String, nullable=True)
    # waterFreq = Column(String, nullable=True) # this should be a enum of some sort
    # imageUrl = Column(String, nullable=True)
    # notes = Column(String, nullable=True)