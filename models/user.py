from db.db import Base
from sqlalchemy import Column, Integer, String, Text, Boolean


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    nickname = Column(String(50))
    user_thumbnail_url = Column(Text)
    veloog_id = Column(String(50))
    email_show = Column(String(50))
    github_show = Column(String(50))
    twitter_show = Column(String(50))
    facebook_show = Column(String(50))
    homepage_show = Column(String(50))
    email = Column(String(50))
    receive_email = Column(Boolean, default=True)
