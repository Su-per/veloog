from pydantic import BaseModel

class SendMail(BaseModel):
    email: str

class SignupEmail(BaseModel):
    nickname: str
    bio: str
    veloog_id: str
    code: str