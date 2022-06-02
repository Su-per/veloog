from fastapi import APIRouter
from api.main import trending, recent

api_router = APIRouter()
api_router.include_router(trending.router)
api_router.include_router(recent.router)