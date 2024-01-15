from typing import List

from fastapi import Depends, HTTPException, APIRouter
from project.common import get_current_user

from project.database import User, Movie, UserReview
from project.schemas import ReviewRequestModel, ReviewRequestPutModel, ReviewResponseModel

router = APIRouter()


@router.get('/reviews', response_model=List[ReviewResponseModel])
async def get_reviews(page: int = 1, limit: int = 10):
  # reviews = UserReview.select() # SELECT * FROM users_reviews
  reviews = UserReview.select().paginate(page, limit)


  return reviews

@router.get('/reviews/{review_id}', response_model=ReviewResponseModel)
async def get_review(review_id: int):
  review = UserReview.select().where(UserReview.id == review_id).first()

  if review is None:
    raise HTTPException(404, 'La review no existe')

  return review

@router.put('/reviews/{review_id}', response_model=ReviewResponseModel)
async def update_review(review_id: int, review: ReviewRequestPutModel, user: User = Depends(get_current_user)):
  review_db = UserReview.select().where(UserReview.id == review_id).first()

  if review_db is None:
    raise HTTPException(404, 'La review no existe')

  if review_db.user_id != user.id:
    raise HTTPException(403, 'No tienes permisos para editar esta review')

  review_db.review = review.review
  review_db.score = review.score

  review_db.save()

  return review

@router.post('/reviews', response_model=ReviewResponseModel)
async def create_review(user_review: ReviewRequestModel, user: User = Depends(get_current_user)):
  
  if Movie.select().where(Movie.id == user_review.movie_id).first() is None:
    raise HTTPException(404, 'La pelicula no existe')

  user_review = UserReview.create(
    user_id=user.id,
    movie_id=user_review.movie_id,
    review=user_review.review,
    score=user_review.score 
  )

  return user_review

@router.delete('/reviews/{review_id}', response_model=ReviewResponseModel)
async def delete_review(review_id: int, user: User = Depends(get_current_user)):
  review = UserReview.select().where(UserReview.id == review_id).first()

  if review is None:
    raise HTTPException(404, 'La review no existe')

  if review.user_id != user.id:
    raise HTTPException(403, 'No tienes permisos para eliminar esta review')

  review.delete_instance()

  return review