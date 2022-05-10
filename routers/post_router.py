from fastapi import APIRouter, Depends
from fastapi_versioning import version
from database import Session

router = APIRouter()

@router.get("/post/{post_id}")
@version(1)
def get_post(post_id: int, db: Session = Depends(Session)):
    result = {}
    db.execute(f"SELECT * FROM post WHERE post_id = {post_id}")
    db.cache = db.cache[0]
    result["id"] = db.cache[0]
    result["writer_id"] = db.cache[1]
    result["description"] = db.cache[4]
    result["date"] = str(db.cache[5])[:10]
    result["likes"] = db.cache[6]
    result["content"] = db.cache[7]
    result["tag"] = db.cache[8].split(",")
    db.execute(f"SELECT * FROM user WHERE user_id = {db.cache[1]}")
    db.cache = db.cache[0]
    result["writer_nickname"] = db.cache[1]
    result["user_thumbnail_url"] = db.cache[2]
    result["veloog_id"] = db.cache[3]
    result["show_email"] = db.cache[4]
    result["show_github"] = db.cache[5]
    result["show_twitter"] = db.cache[6]
    result["show_facebook"] = db.cache[7]
    result["email"] = db.cache[8]
    return result