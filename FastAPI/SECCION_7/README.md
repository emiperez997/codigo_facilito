# Notas Sección 7 - Autenticación OAuth2

## Introducción al bloque OAuth2

¿Qué es OAuth2?

- Es un estándar abierto para la autorización de aplicaciones web
- Pudiendo así asegurar recursos para nuestra API

4 entidades:

- Recurso protegido
- Cliente
- Dueño del recurso
- Servidor de autorización

Pasos a seguir

- El usuario ingresa sus credenciales
- El servidor verifica que las credenciales sean correctas y retnorarn un Web Token
- El token es guardado por el cliente
- Las nuevas peticiones realizadas por el cliente debe enviar el token obtenido
- El servidor valida el token y retorna el recurso protegido

JSON Web Token (JWT)

- Cadena alfanumérica Stateless
- Contiene información que por sí misma valida su autenticidad

¿Por qué no usar solo Cookies?

- No todos los clientes soportan el uso de cookies. Entre más clientes puedan utilizar nuestra API mucho mejor
- Un mayor performance en la comunicación entre cliente y servidor

## Login

Agregamos el siguiente endpoint en el archivo `__init__.py`:

```python
@app.post("/auth")
async def auth(data: OAuth2PasswordRequestForm = Depends()):
  user = User.authenticate(data.username, data.password)

  if user:
    return {
      "username": data.username,
      "password": data.password
    }
  else:
    raise HTTPException(
      status_code=401,
      detail='Usuario o contraseña incorrectos',
      headers={"WWW-Authenticate": "Bearer"})
```

Y creamos el metodo de clase:

```python
class User(Model):
  ...
    @classmethod
  def authenticate(cls, username, password):
    user = cls.select().where(User.username == username).first()

    if user and user.password == cls.create_password(password):
      return user
  ...
```

## Generar access token

Para generar el access token, instalamos la libreria `pyjwt`:

```bash
pip install pyjwt
```

Creamos el metodo en el archivo `common.py`:

```python
def create_access_token(user, hours=10):
  data = {
    "user_id": user.id,
    "username": user.username,
    "exp": datetime.utcnow() + timedelta(hours=hours)
  }

  return jwt.encode(data, SECRET_KEY, algorithm='HS256')
```

## Endpoints restringidos

Para restringir un endpoint, importamos la libreria `Depends` y hacer que dependa del modelo de OAuth2 que nosotros definamos (en nuestro caso es `OAuth2PasswordBearer`):

```python
# Archivo common.py

# tokenUrl es el endpoint que se encarga de generar el token
OATUH2_SCHEMA = OAuth2PasswordBearer(tokenUrl='/api/auth')

# Archivo users_routes.py
# Depends: depende del modelo de OAuth2 que nosotros definamos
@router.get('/reviews')
async def get_review(token: str = Depends(OATUH2_SCHEMA)):
  return {
    'token': token
  }
```
