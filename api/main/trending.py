from fastapi import APIRouter, Depends
from db.session import session
from models.post import Post

router = APIRouter()


@router.get("/trending")
async def trending(pages: int = 0, session=Depends(session)):
    print(session.query(Post).order_by(Post.post_id).all())
