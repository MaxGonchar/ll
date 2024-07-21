from pydantic import BaseModel


class SignOnResponse(BaseModel):
    access_token: str
    refresh_token: str


class SignOnRequest(BaseModel):
    first: str
    last: str
    email: str
    psw: str
