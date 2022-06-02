from fastapi import APIRouter
from fastapi_sqlalchemy import db
from models.post import Post
from models.reply import Reply
from models.user import User

router = APIRouter()


@router.get("/recent")
async def recent(pages: int = 0):
    result = []
    for i in db.session.query(Post).offset(pages * 20).limit((pages + 1) * 20).all():

        reply_count = db.session.query(Reply).filter_by(target_id=i.post_id).count()
        writer_nickname = db.session.query(User.nickname).filter_by(user_id=i.writer_id).first()
        writer_profile_url = db.session.query(User.user_thumbnail_url).filter_by(user_id=i.writer_id).first()

        result.append(
            {
                "post_id": i.post_id,
                "writer_id": i.writer_id,
                "title": i.title,
                "post_thumbnail_url": i.post_thumbnail_url,
                "description": i.description,
                "date": i.date,
                "like": i.like,
                "reply_count": reply_count,
                "writer_nickname": writer_nickname,
                "writer_profile_url": writer_profile_url,
            }
        )

    return result
