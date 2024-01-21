from datetime import datetime,timedelta
from typing import Optional
from jose import jwt

from app.core.config import Settings


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=Settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, Settings.SECRET_KEY, algorithm=Settings.ALGORITHM)
    
    return encoded_jwt