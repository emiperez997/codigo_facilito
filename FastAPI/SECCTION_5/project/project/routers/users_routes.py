from fastapi import APIRouter, HTTPException
from project.database import User
from project.schemas import UserRequestModel, UserResponseModel

from fastapi.security import HTTPBasicCredentials

router = APIRouter()

@router.post('/users', response_model=UserResponseModel)
async def create_user(user: UserRequestModel):
  # Validar si el usuario ya existe
  if User.select().where(User.username == user.username).exists():
    return HTTPException(409, 'El username ya existe')

  hash_password = User.create_password(user.password)

  user = User.create(username=user.username, password=hash_password)
  
  return UserResponseModel(id=user.id, username=user.username)

@router.post('/login', response_model=UserResponseModel)
async def login(credentials: HTTPBasicCredentials):
  user = User.select().where(User.username == credentials.username).first()

  if user is None:
    raise HTTPException(404, 'El usuario no existe')

  if user.password != User.create_password(credentials.password):
    raise HTTPException(404, 'El password es incorrecto')

  return user