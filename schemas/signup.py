from pydantic import BaseModel

class SendMail(BaseModel):
    email: str