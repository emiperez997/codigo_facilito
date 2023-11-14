from urllib import request

URL = 'http://localhost:8000'

response = request.urlopen(URL) # Hacer la petición
# print(response.__dict__) # Ver los atributos del objeto
print(response.read()) # Leer la respuesta