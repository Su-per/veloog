from fastapi import APIRouter
from api.main import trending, recent
from api.signup import signup_email, signup_facebook, signup_google, signup_github

api_router = APIRouter()
api_router.include_router(trending.router)
api_router.include_router(recent.router)

api_router.include_router(signup_email.router)
api_router.include_router(signup_facebook.router)
api_router.include_router(signup_google.router)
api_router.include_router(signup_github.router)