from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative
from typing import Any


@as_declarative()
class Base:
    id: Any
    is_active = Column(Boolean(), default=True)
    create_time = Column(DateTime, default=datetime.now)
    last_update_time = Column(DateTime, default=datetime.now)
    __name__: str

    #to generate tablename from classname
    @declared_attr 
    def __tablename__(cls) -> str:
        return cls.__name__.lower()