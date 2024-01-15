from typing import List
from fastapi import APIRouter, HTTPException, Response
from fastapi import Cookie

from project.database import User
from project.schemas import ReviewResponseModel, UserRequestModel, UserResponseModel

from fastapi.security import HTTPBasicCredentials

router = APIRouter(prefix='/users')

@router.post('/', response_model=UserResponseModel)
async def create_user(user: UserRequestModel):
  # Validar si el usuario ya existe
  if User.select().where(User.username == user.username).exists():
    return HTTPException(409, 'El username ya existe')

  hash_password = User.create_password(user.password)

  user_db = User.create(username=user.username, password=hash_password)
  
  return UserResponseModel(id=user_db.id, username=user_db.username) 

@router.post('/login', response_model=UserResponseModel)
async def login(credentials: HTTPBasicCredentials, response: Response):
  user = User.select().where(User.username == credentials.username).first()

  if user is None:
    raise HTTPException(404, 'El usuario no existe')

  if user.password != User.create_password(credentials.password):
    raise HTTPException(404, 'El password es incorrecto')

  response.set_cookie(key='user_id', value=user.id) 

  # También se puede enviar un token en la cookie
  # response.set_cookie(key='token', value=token)
  return user

@router.get('/reviews', response_model=List[ReviewResponseModel])
async def get_reviews(user_id: int = Cookie(None)): # Cookie(None) significa que el valor es opcional
  # Si no se envía el user_id en la cookie, se devuelve None
  user = User.select().where(User.id == user_id).first() # type: ignore

  if user is None:
    raise HTTPException(404, 'El usuario no existe')

  return [user_review for user_review in user.reviews]