# Create server
from wsgiref.simple_server import make_server

HTML = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Server HTML</title>
  </head>
  <body>
    <h1>Hola mundo desde el servidor de Python</h1>
  </body>
</html>
"""

def application(env, start_response): 
  
  headers = [('Content-Type', 'text/html')]

  start_response('200 OK', headers)
  
  return [bytes(HTML, 'utf-8')] # Convertir a bytes

server = make_server('localhost', 8000, application)
server.serve_forever()