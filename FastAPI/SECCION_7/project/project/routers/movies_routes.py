from typing import List
from fastapi import APIRouter
from project.database import Movie

from project.schemas import MovieRequestModel, MovieResponseModel

router = APIRouter()

@router.post('/movies', response_model=MovieResponseModel)
async def create_movie(movie: MovieRequestModel):
  movie = Movie.create(title=movie.title)

  return movie

@router.get('/movies', response_model=List[MovieResponseModel])
async def get_movies():
  movies = Movie.select()

  return movies