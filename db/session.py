from core.config import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(settings.SQLALCHEMY_DB_URL, echo=False)
Session = sessionmaker()
Session.configure(bind=engine)


def session():
    return Session()
