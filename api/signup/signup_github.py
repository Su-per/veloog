from fastapi import APIRouter
from fastapi_sqlalchemy import db


router = APIRouter()


@router.post("/signup/github")
async def signup_github():
    pass