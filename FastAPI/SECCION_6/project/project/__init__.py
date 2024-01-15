from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from .database import Movie, User, UserReview
from .database import database as connection

from typing import List

# from .schemas import UserRequestModel, UserResponseModel
# from .schemas import ReviewRequestModel, ReviewResponseModel, ReviewRequestPutModel
# from .schemas import MovieRequestModel, MovieResponseModel

from .routers import router

app = FastAPI(title="My first API", description="This is a very fancy project", version="1.0.0")

# Eventos
# Startup - Shutdown
# use lifespan
# @app.on_event('startup')
# def startup():
#   if connection.is_closed():
#     connection.connect()

#   # Crear tablas si no existen
#   # Si existen, no hace nada
#   connection.create_tables([User, Movie, UserReview]) 

# @app.on_event('shutdown')
# def shutdown():
#   if not connection.is_closed():
#     connection.close()

# Eventos (nueva version)
@asynccontextmanager
async def database_connection():
  if connection.is_closed():
    connection.connect()

  try:
    yield
  finally:
    if not connection.is_closed():
      connection.close()


@app.get("/")
async def index():
    return {"message": "Hello world!"}

app.include_router(router, prefix='/api')


# @app.get("/about")
# async def about():
#     return {"message": "This is a very fancy project"}

# # Response model: UserResponseModel | Indicar que el response es un UserResponseModel
# @app.post('/users', response_model=UserResponseModel)
# async def create_user(user: UserRequestModel):
#   # Validar si el usuario ya existe
#   if User.select().where(User.username == user.username).exists():
#     return HTTPException(409, 'El username ya existe')

#   hash_password = User.create_password(user.password)

#   user = User.create(username=user.username, password=hash_password)
  
#   return UserResponseModel(id=user.id, username=user.username)

# @app.post('/movies', response_model=MovieResponseModel)
# async def create_movie(movie: MovieRequestModel):
#   movie = Movie.create(title=movie.title)

#   return movie

# Reviews
# @app.get('/reviews', response_model=List[ReviewResponseModel])
# async def get_reviews(page: int = 1, limit: int = 10):
#   # reviews = UserReview.select() # SELECT * FROM users_reviews
#   reviews = UserReview.select().paginate(page, limit)


#   return reviews

# @app.get('/reviews/{review_id}', response_model=ReviewResponseModel)
# async def get_review(review_id: int):
#   review = UserReview.select().where(UserReview.id == review_id).first()

#   if review is None:
#     raise HTTPException(404, 'La review no existe')

#   return review

# @app.put('/reviews/{review_id}', response_model=ReviewResponseModel)
# async def update_review(review_id: int, review: ReviewRequestPutModel):
#   review = UserReview.select().where(UserReview.id == review_id).first()

#   if review is None:
#     raise HTTPException(404, 'La review no existe')

#   review.review = review.review
#   review.score = review.score

#   review.save()

#   return review

# @app.post('/reviews', response_model=ReviewResponseModel)
# async def create_review(user_review: ReviewRequestModel):

#   if User.select().where(User.id == user_review.user_id).first() is None:
#     raise HTTPException(404, 'El usuario no existe')

#   if Movie.select().where(Movie.id == user_review.movie_id).first() is None:
#     raise HTTPException(404, 'La pelicula no existe')

#   user_review = UserReview.create(
#     user_id=user_review.user_id,
#     movie_id=user_review.movie_id,
#     review=user_review.review,
#     score=user_review.score 
#   )

#   return user_review

# @app.delete('/reviews/{review_id}', response_model=ReviewResponseModel)
# async def delete_review(review_id: int):
#   review = UserReview.select().where(UserReview.id == review_id).first()

#   if review is None:
#     raise HTTPException(404, 'La review no existe')

#   review.delete_instance()

#   return review