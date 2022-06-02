from fastapi import APIRouter
from fastapi_sqlalchemy import db
from schemas.signup import SendMail
import hashlib
from models.auth import Auth


router = APIRouter()


@router.post("/signup/email/sendmail")
async def signup_email_sendmail(sendmail: SendMail):
    email = sendmail.email
    code = hashlib.sha256(email.encode()).hexdigest()
    db.session.add(Auth(email=email, code=code))
    db.session.commit()
    return {"code": code}