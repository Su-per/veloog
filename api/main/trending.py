from fastapi import APIRouter
from fastapi_sqlalchemy import db
from models.post import Post

router = APIRouter()


@router.get("/trending")
async def trending(pages: int = 0):
    print(db.session.query(Post).all())
