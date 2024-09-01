import json
from datetime import UTC, datetime
from unittest.mock import patch

from flask_jwt_extended import decode_token

import src.controllers.auth_controllers as subj
from src import app
from src.models.user import User
from src.schema.auth import SignOnRequest


def assert_access_token_in_response(response: dict, user_id: str) -> None:
    assert "access_token" in response
    assert_token_content(response["access_token"], user_id)
    assert response["access_token"] is not None


def assert_refresh_token_in_response(response: dict, user_id: str) -> None:
    assert "refresh_token" in response
    assert_token_content(response["refresh_token"], user_id)
    assert response["access_token"] is not None


def assert_token_content(token: str, user_id: str) -> None:
    with app.app_context():
        token_content = decode_token(token)
    assert token_content["sub"] == user_id
    assert "exp" in token_content


def assert_user_obj(user_obj: User, user: User) -> None:
    assert user_obj.id == user.id
    assert user_obj.first == user.first
    assert user_obj.last == user.last
    assert user_obj.email == user.email
    assert user_obj.role == user.role
    assert user_obj.last_login == user.last_login
    assert user_obj.password_hash is not None


def test_register() -> None:
    user = SignOnRequest(
        first="first",
        last="last",
        email="email",
        psw="password",
    )
    user_id = "d1a0661e-2339-4dcc-8a87-9a7ffe0e3731"

    last_login = datetime(2024, 8, 11, 13, 56, 56, 642916, tzinfo=UTC)

    with (
        patch(
            "src.controllers.auth_controllers.repo.add_user",
        ) as mock_add_user,
        patch("src.controllers.auth_controllers.uuid4", return_value=user_id),
        patch(
            "src.controllers.auth_controllers.get_current_time",
            return_value=last_login,
        ),
        app.app_context(),
    ):
        actual = subj.register(user)

    actual = json.loads(actual)
    assert_access_token_in_response(actual, user_id)
    assert_refresh_token_in_response(actual, user_id)

    expected_user_obj_to_add = User(
        id=user_id,
        first=user.first,
        last=user.last,
        email=user.email,
        role="default_roleq",
        last_login=last_login,
    )
    actual_user_obj_to_add = mock_add_user.call_args.args[0]
    assert_user_obj(actual_user_obj_to_add, expected_user_obj_to_add)
