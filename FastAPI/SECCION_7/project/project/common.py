from datetime import datetime
from datetime import timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt

from .database import User

SECRET_KEY = 'CodigoFacilito2024'

OATUH2_SCHEMA = OAuth2PasswordBearer(tokenUrl='/api/auth')

def create_access_token(user, hours=10):
  data = {
    "user_id": user.id,
    "username": user.username,
    "exp": datetime.utcnow() + timedelta(hours=hours) 
  }

  return jwt.encode(data, SECRET_KEY, algorithm='HS256')

def decode_access_token(token):
  try:
      return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
  except Exception as err:
     return None


def get_current_user(token: str = Depends(OATUH2_SCHEMA)) -> User:
  data = decode_access_token(token)

  if data:
       return User.select().where(User.id == data['user_id']).first()
  else:
     raise HTTPException(
        status_code=401,
        detail="Access token invalido",
        headers={"WWW-Authenticate": "Bearer"},
     )

