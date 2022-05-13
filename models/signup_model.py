from pydantic import BaseModel


class SignupReq(BaseModel):
    email: str = "email"


class SignupRedirectReq(BaseModel):
    nickname: str = "nickname"
    id: str = "id"
    bio: str = "bio"


class SignupRes(BaseModel):
    message: str = "Success"
    code: str = "temporary code"


class SignupRedirectRes(BaseModel):
    message: str = "Success"
