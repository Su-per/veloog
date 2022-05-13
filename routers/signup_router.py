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


def sendMail(email: str, code: str):
    msg = MIMEText("http://localhost/api/v1/signup?code=" + code)
    msg["Subject"] = "veloog 계정 인증"
    s.sendmail("juyoon7163@gmail.com", email, msg.as_string())


@router.post("/signup", response_model=SignupRes, tags=["signup"])
@version(1)
def signup(req: SignupReq, send_mail: BackgroundTasks, db: Session = Depends(Session)):
    code = hashlib.md5(req.email.encode()).hexdigest()
    db.execute(f"INSERT INTO email_auth VALUES('{req.email}', '{code}')")
    send_mail.add_task(sendMail, req.email, code)
    return {"message": "success", "code": code}


@router.post("/signup/redirect", response_model=SignupRedirectRes, tags=["signup"])
@version(1)
def signup_redirect(req: SignupRedirectReq, code: str, db: Session = Depends(Session)):
    db.execute(f"SELECT * FROM email_auth WHERE code = '{code}'")
    print(db.cache)
    email = db.cache[0][0]
    if len(db.cache) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="인증 코드 또는 이메일이 올바르지 않습니다.",
        )
    db.execute(f"DELETE FROM email_auth WHERE code = '{code}'")
    if len(db.execute(f"SELECT email FROM user WHERE email = '{email}'")) != 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="중복된 이메일입니다."
        )
    if len(db.execute(f"SELECT veloog_id FROM user WHERE veloog_id = '{req.id}'")) != 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="중복된 아이디입니다."
        )
    db.execute(
        f"INSERT INTO user VALUES(NULL, '{req.nickname}', 'Default Thumbnail', '{req.id}', '{req.bio}', '','','','','', '{email}', 1)"
    )
