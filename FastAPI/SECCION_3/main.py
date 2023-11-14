# Create server
from wsgiref.simple_server import make_server

# Response las peticiones del cliente
def application(env, start_response): 
  # env → Diccionario de información de la petición
  # start_response → Función para enviar el status y las cabeceras
  print(env)
  headers = [('Content-Type', 'text/plain')] # Encabezados

  start_response('200 OK', headers)

  # Se retorna un listado de cadenas de bytes
  return ["Hola mundo desde el servidor de Python".encode("utf-8")] # Codificamos la respuesta como una lista

server = make_server('localhost', 8000, application) # Creamos el servidor
server.serve_forever() # Lo ponemos a escuchar