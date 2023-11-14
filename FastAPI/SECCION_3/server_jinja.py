# Create server
from re import template
from wsgiref.simple_server import make_server

# Imports jinja2
from jinja2 import Environment, FileSystemLoader

def application(env, start_response): 
  
  headers = [('Content-Type', 'text/html')]

  start_response('200 OK', headers)

  env = Environment(loader=FileSystemLoader('templates')) # Cargar los templates
  template = env.get_template('index.html') # Obtener el template

  html = template.render(
    {
      'title': 'Server Jinja',
      'name': 'Jinja',
    }
  )
  
  return [bytes(html, 'utf-8')] # Convertir a bytes

server = make_server('localhost', 8000, application)
server.serve_forever()