from fastapi import APIRouter
from project.database import Movie

from project.schemas import MovieRequestModel, MovieResponseModel

router = APIRouter()

@router.post('/movies', response_model=MovieResponseModel)
async def create_movie(movie: MovieRequestModel):
  movie = Movie.create(title=movie.title)

  return movie