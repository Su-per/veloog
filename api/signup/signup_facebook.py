from fastapi import APIRouter
from fastapi_sqlalchemy import db


router = APIRouter()


@router.post("/signup/facebook")
async def signup_facebook():
    pass