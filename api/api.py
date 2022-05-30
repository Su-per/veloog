from fastapi import APIRouter
from api.main import trending

api_router = APIRouter()
api_router.include_router(trending.router)