import hashlib
from peewee import MySQLDatabase
from peewee import CharField, DateTimeField, ForeignKeyField, IntegerField, Model, TextField
from datetime import datetime

database = MySQLDatabase('fastapi_project', user='root', password='root', host='localhost', port=3306)

# Modelos
class User(Model):
  username = CharField(max_length=50, unique=True) 
  password = CharField(max_length=50)
  created_at = DateTimeField(default=datetime.now)

  def __str__(self):
    return self.username

  # Configuracion de la clase
  class Meta:
    database = database
    table_name = 'users'

  # Metodos de la clase
  @classmethod
  def create_password(cls, password):
    h = hashlib.md5()
    password = h.update(password.encode('utf-8'))
    return h.hexdigest()

  @classmethod
  def authenticate(cls, username, password):
    user = cls.select().where(User.username == username).first()

    if user and user.password == cls.create_password(password):
      return user 
  

class Movie(Model):
  title = CharField(max_length=50)
  created_at = DateTimeField(default=datetime.now)

  def __str__(self):
    return self.title

  # Configuracion de la clase
  class Meta:
    database = database
    table_name = 'movies'

class UserReview(Model):
  user = ForeignKeyField(User, backref='reviews')
  movie = ForeignKeyField(Movie, backref='reviews')
  review = TextField()
  score = IntegerField()
  created_at = DateTimeField(default=datetime.now)

  def __str__(self):
    return f'{self.user} - {self.movie}'

  # Configuracion de la clase
  class Meta:
    database = database
    table_name = 'users_reviews'