
from pydantic import BaseModel, validator
from typing import Optional

class User(BaseModel):
  # Atributos requeridos
  username: str
  password: str
  repeat_password: str
  email: str
  age: Optional[int] = None

  # Custom validations
  @validator('username')
  def username_validation_length(cls, username):
    if len(username) < 3:
      raise ValueError('El username debe tener al menos 3 caracteres')

    if len(username) > 50:
      raise ValueError('El username no puede tener mas de 50 caracteres')

    return username

  @validator('repeat_password')
  def repeat_password_validation(cls, repeat_password, values):
    if 'password' in values and repeat_password != values['password']:
      raise ValueError('Las contraseñas no coinciden')

    return repeat_password
    
try:
  user1 = User(username="Jose", repeat_password="12345", password="1234", email="jose@gmail.com", edad= 21)

  print(user1)

except ValueError as error:
  print(error.json())
