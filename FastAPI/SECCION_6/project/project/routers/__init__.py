from fastapi import APIRouter

from project.routers.users_routes import router as users_router
from project.routers.movies_routes import router as movies_router
from project.routers.reviews_routes import router as reviews_router

router = APIRouter()

router.include_router(users_router, tags=['Users'])
router.include_router(movies_router, tags=['Movies'])
router.include_router(reviews_router, tags=['Reviews'])
