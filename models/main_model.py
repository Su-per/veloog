from pydantic import BaseModel


class MainRes(BaseModel):
    result: list = [
        {
            "id": "post_id",
            "writer_id": "writer_id",
            "title": "title",
            "post_thumbnail_url": "post_thumbnail_url",
            "description": "description",
            "date": "date",
            "likes": "likes",
            "contnet": "contnet",
        }
    ]
