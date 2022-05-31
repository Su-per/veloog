from fastapi import APIRouter, Depends
from db.session import get_db
from models.post import Post
from sqlalchemy import select
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/trending")
async def trending(pages: int = 0, db: Session = Depends(get_db)):
    print(db)
