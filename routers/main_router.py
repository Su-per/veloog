from fastapi import APIRouter, Depends
from fastapi_versioning import version
from database import Session

router = APIRouter()


@router.get("/trending")
@version(1)
def trending(page: int = 0, db: Session = Depends(Session)):
    result = []
    for data in db.execute(
        f"SELECT * FROM post ORDER BY likes DESC LIMIT {page*20 + 1}, {(page+1) * 20}"
    ):
        result.append(
            {
                "id": data[0],
                "writer_id": data[1],
                "title": data[2],
                "post_thumbnail_url": data[3],
                "description": data[4],
                "date": str(data[5])[:10],
                "likes": data[6],
                "contnet": data[7],
                "tag": data[8].split(","),
            }
        )
    return result


@router.get("/recent")
@version(1)
def recent(page: int, db: Session = Depends(Session)):
    result = []
    for data in db.execute(
        f"SELECT * FROM post ORDER BY date DESC LIMIT {page*20 + 1}, {(page+1) * 20}"
    ):
        result.append(
            {
                "id": data[0],
                "writer_id": data[1],
                "title": data[2],
                "post_thumbnail_url": data[3],
                "description": data[4],
                "date": str(data[5])[:10],
                "likes": data[6],
                "contnet": data[7],
                "tag": data[8].split(","),
            }
        )
    return result
