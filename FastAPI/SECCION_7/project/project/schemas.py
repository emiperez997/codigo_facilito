from typing import Any
from pydantic import BaseModel, field_validator, ConfigDict
# v1 → version 1
from pydantic.v1.utils import GetterDict

from peewee import ModelSelect

# GetterDict
# class PeeweeGetterDict(GetterDict):
#   def get(self, key: Any, default: Any = None):
#     res = getattr(self._obj, key, default)
    
#     if isinstance(res, ModelSelect):
#       return list(res)

#     return res

class ResponseModel(BaseModel):
  # Nueva forma de parsear los modelos de peewee a pydantic
  model_config = ConfigDict(from_attributes=True)

  # Forma antigua de parsear los modelos de peewee a pydantic
  # class Config:
  #   from_attributes = True
  #   model_getter = PeeweeGetterDict

# -------- User -------- #
class UserRequestModel(BaseModel): 
  username: str
  password: str

  @field_validator('username')
  def username_validator(cls, username):
    if len(username) < 3:
      raise ValueError('El username debe tener al menos 3 caracteres')

    if len(username) > 50:
      raise ValueError('El username no puede tener mas de 50 caracteres')

    return username

  @field_validator('password')
  def password_validator(cls, password):
    if len(password) < 3:
      raise ValueError('La contraseña debe tener al menos 3 caracteres')

    if len(password) > 10:
      raise ValueError('La contraseña no puede tener mas de 10 caracteres')

    if not any(char.isdigit() for char in password):
      raise ValueError('La contraseña debe contener al menos un numero')
    
    if not any(char.isalpha() for char in password):
      raise ValueError('La contraseña debe contener al menos un caracter')

    return password
  
class UserResponseModel(ResponseModel):
  id: int
  username: str

# -------- Movie -------- #

class MovieRequestModel(BaseModel):
  title: str

class MovieResponseModel(ResponseModel):
  id: int
  title: str

# -------- Review -------- #
class ReviewValidator():
  @field_validator('score')
  def score_validator(cls, score):
    if score < 0 or score > 5:
      raise ValueError('El score debe estar entre 1 y 5')

    return score

class ReviewRequestModel(BaseModel, ReviewValidator):
  movie_id: int
  review: str
  score: int

class ReviewResponseModel(ResponseModel):
  id: int
  movie: MovieResponseModel
  review: str
  score: int

class ReviewRequestPutModel(BaseModel, ReviewValidator):
  review: str
  score: int
