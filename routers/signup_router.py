from fastapi import APIRouter, Depends, BackgroundTasks, status, HTTPException
from fastapi_versioning import version
from database import Session
from models.signup_model import (
    SignupReq,
    SignupRedirectReq,
    SignupRes,
    SignupRedirectRes,
)
import smtplib
from email.mime.text import MIMEText
import hashlib

router = APIRouter()

s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login("juyoon7163@gmail.com", "jpzfsywshwyyichj")


def sendMail(email: str):
    msg = MIMEText("ㅋㅋ")
    msg["Subject"] = "veloog 계정 인증"
    s.sendmail("juyoon7163@gmail.com", email, msg.as_string())


@router.post("/signup", response_model=SignupRes)
@version(1)
def signup(req: SignupReq, send_mail: BackgroundTasks, db: Session = Depends(Session)):
    code = hashlib.md5(req.email.encode()).hexdigest()
    db.execute(f"INSERT INTO email_auth VALUES(NULL, {req.email}, {code}, 0)")
    send_mail.add_task(sendMail, req.email)
    return {"message": "success", "code": code}


@router.post("/signup/redirect", response_model=SignupRedirectRes)
@version(1)
def signup_redirect(req: SignupRedirectReq, code: str, db: Session = Depends(Session)):
    db.execute(f"SELECT * FROM email_auth WHERE code = {code} AND email = {req.email}")
    if len(db.cache) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="인증 코드 또는 이메일이 올바르지 않습니다.",
        )
    db.execute(f"DELETE FROM email_auth WHERE code = {code} AND email = {req.email}")
