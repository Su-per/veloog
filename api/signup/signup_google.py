from fastapi import APIRouter
from fastapi_sqlalchemy import db


router = APIRouter()


@router.post("/signup/google")
async def signup_google():
    pass