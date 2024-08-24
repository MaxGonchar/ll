from pydantic import BaseModel


class SignOnResponse(BaseModel):
    access_token: str
    refresh_token: str


# TODO(MaxGonchar): Add validation to the schema
class SignOnRequest(BaseModel):
    first: str
    last: str
    email: str
    psw: str
