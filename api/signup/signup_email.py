from os import stat
from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db
from schemas.signup import SendMail, SignupEmail
import hashlib
from models.auth import Auth
from models.user import User
from utils import validate


router = APIRouter()


@router.post("/signup/email/sendmail")
async def signup_email_sendmail(sendmail: SendMail):
    email = sendmail.email
    code = hashlib.sha256(email.encode()).hexdigest()
    db.session.add(Auth(email=email, code=code))
    db.session.commit()
    return {"code": code}

@validate
@router.post("/signup/email")
async def signup_email(signup_email: SignupEmail):
    code = db.session.query(Auth.code).filter_by(code=signup_email.code).first()
    if code == None:
        raise HTTPException(status_code=400, detail="잘못된 코드입니다.")
    else:
        email = db.session.query(Auth.email).filter_by(code=signup_email.code).first()[0]
        db.session.query(Auth).filter_by(code=signup_email.code).delete()
        db.session.add(User(
            nickname=signup_email.nickname, 
            bio=signup_email.bio, 
            veloog_id=signup_email.veloog_id, 
            email=email
        ))
        db.session.commit()
