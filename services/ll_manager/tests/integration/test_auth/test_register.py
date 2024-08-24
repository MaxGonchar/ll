import http

import jwt
import requests

HOST = "http://localhost:5000"
BASE_URL = f"{HOST}/auth/register"


def get_user_from_jwt(my_jwt: str) -> str:
    claims = jwt.decode(
        my_jwt,
        options={"verify_signature": False},
        algorithms=["HS256"],
    )
    return claims["sub"]


# TODO(MaxGonchar): clean db before running this test
def test_register() -> None:
    payload = {
        "first": "first",
        "last": "last",
        "email": "email",
        "psw": "password",
    }
    resp = requests.post(BASE_URL, json=payload, timeout=10)

    assert resp.status_code == http.HTTPStatus.CREATED, resp.text
    payload = resp.json()
    assert "access_token" in payload, payload
    assert "refresh_token" in payload, payload
