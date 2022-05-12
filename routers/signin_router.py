from fastapi import APIRouter, Depends, BackgroundTasks, status, HTTPException
from fastapi_versioning import version
from database import Session
import smtplib
from email.mime.text import MIMEText

router = APIRouter()

s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login("juyoon7163@gmail.com", "jpzfsywshwyyichj")


def sendMail(email: str, code: str):
    msg = MIMEText("http://localhost/api/v1/signup?code=" + code)
    msg["Subject"] = "veloog 계정 인증"
    s.sendmail("juyoon7163@gmail.com", email, msg.as_string())


@router.post("/signin")
@version(1)
def signin(send_mail: BackgroundTasks, db: Session = Depends(Session)):
    pass
