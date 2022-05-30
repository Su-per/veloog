from db.db import Base
from sqlalchemy import Column, Integer, Text, Date


class Post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True)
    writer_id = Column(Integer)
    title = Column(Text)
    post_thumbnail_url = Column(Text)
    description = Column(Text)
    date = Column(Date)
    like = Column(Integer)
    content = Column(Text)
    tag = Column(Text)
