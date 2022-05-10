from fastapi import APIRouter, Depends
from fastapi_versioning import version
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

@router.get("/")
@version(1)
async def users(db: Session = Depends(get_db)):
    return