from pydantic import BaseModel


class SignupReq(BaseModel):
    email: str


class SignupRedirectReq(BaseModel):
    nickname: str
    id: str
    bio: str


class SignupRes(BaseModel):
    message: str
    code: str


class SignupRedirectRes(BaseModel):
    message: str
