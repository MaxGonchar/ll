import jwt
import requests

HOST = "http://localhost:5000"
BASE_URL = f"{HOST}/auth/register"


def get_user_from_jwt(my_jwt: str) -> str:
    claims = jwt.decode(my_jwt, options={'verify_signature': False}, algorithms=["HS256"])
    return claims["sub"]


# TODO: clean db before running this test
def test_register():
    payload = {
        "first": "first",
        "last": "last",
        "email": "email",
        "psw": "password",
    }
    resp = requests.post(BASE_URL, json=payload)

    assert resp.status_code == 201
    payload = resp.json()
    assert "access_token" in payload
    assert "refresh_token" in payload
