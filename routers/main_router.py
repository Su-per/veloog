from fastapi import APIRouter, Depends
from fastapi_versioning import version
from database import Session

router = APIRouter()

@router.get("/trending")
@version(1)
def users(db: Session = Depends(Session), period: str = "week"):
    result = []
    for data in db.execute("SELECT * FROM post"):
        result.append({
            "id": data[0],
            "writer_id": data[1],
            "title": data[2],
            "post_thumbnail_url": data[3],
            "description": data[4],
            "date": data[5],
            "likes": data[6],
            "contnet": data[7],
            "tag": data[8].split(",")
        })
    return result
