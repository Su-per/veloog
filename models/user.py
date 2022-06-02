from email.policy import default
from db.base import Base
from sqlalchemy import Column, Integer, String, Text, Boolean


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    nickname = Column(String(50))
    bio = Column(Text)
    user_thumbnail_url = Column(Text, default='')
    veloog_id = Column(String(50))
    email_show = Column(String(50), default='')
    github_show = Column(String(50), default='')
    twitter_show = Column(String(50), default='')
    facebook_show = Column(String(50), default='')
    homepage_show = Column(String(50), default='')
    email = Column(String(50))
    receive_email = Column(Boolean, default=True)
