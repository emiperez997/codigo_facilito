# Notas

## Conexión a base de datos

Gestor: MySQL
ORM: Peewee

Otros paquetes necesarios (sino tira error):

- pymysql
- cryptography

Ingresar a la base de datos de docker:

```bash
docker exec -i -t <container_id> /bin/bash

mysql -u root -p
Enter password:
```

## Serializar objetos

Con la clase PeeweeGetterDict sirve para convertir un modelo a una clase de respuesta, para que no haya inconvenientes con los objetos de tipo model de peewee

Para pasar modelos de peewee a objetos de pydantic se utiliza la manera actual:

```python
from pydantic import BaseModel, ConfigDict


class ResponseModel(BaseModel):
  model_config = ConfigDict(from_attributes=True)
```

## Paginación

Nos apoyamos a un query set de peewee para poder paginar los resultados de una consulta, para ello se utiliza el método `paginate` de peewee, el cual recibe como parámetros:

## Login

HTTPBasicCredentials es una clase de fastapi que nos permite obtener el usuario y contraseña de un request, para ello se utiliza el método `HTTPBasicCredentials.parse` que recibe como parámetro el header de autorización del request.
