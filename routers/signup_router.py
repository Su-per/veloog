from fastapi import APIRouter, Depends, BackgroundTasks
from fastapi_versioning import version
from database import Session
import smtplib
from email.mime.text import MIMEText

router = APIRouter()
s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login("juyoon7163@gmail.com", "jpzfsywshwyyichj")

def sendMail(email: str, token, nickname):
    msg = MIMEText(
        f"안녕하세요 {nickname}님."
        + token
        + " 에 접속해 이메일 인증을 완료해주세요."
    )
    msg["Subject"] = "[] 계정 인증"
    s.sendmail("juyoon7163@gmail.com", email, msg.as_string())

@router.get("/trending")
@version(1)
def signup_email(send_mail: BackgroundTasks, db: Session = Depends(Session)):
    send_mail.add_task(sendMail, email, token, nickname)