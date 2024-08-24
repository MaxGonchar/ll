# TODO(bobrodede@gmail.com): clear db before running tests
import os
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.sql import text

import src.repos.auth_repo as subj
from src import app
from src.models.user import User


def get_db_user(email: str) -> list[User]:
    # TODO(bobrodede@gmail.com): handle create engine in a better way
    engine = create_engine(
        f'postgresql://{os.environ["POSTGRES_USER"]}:{os.environ["POSTGRES_PASSWORD"]}@{os.environ["POSTGRES_HOST"]}:{os.environ["POSTGRES_PORT"]}/{os.environ["POSTGRES_DB"]}',
    )

    with engine.connect() as con:
        return (
            con.execute(
                text("SELECT * FROM users WHERE email=:email"),
                {"email": email},
            )
            .mappings()
            .all()
        )


def assert_user(user: User, db_user: User) -> None:
    assert user["id"] == str(db_user["id"])
    assert user["first"] == db_user["first"]
    assert user["last"] == db_user["last"]
    assert user["email"] == db_user["email"]
    assert user["role"] == db_user["role"]
    assert user["last_login"] == db_user["last_login"]
    assert db_user["password_hash"] is not None


def test_add() -> None:
    expected_user = {
        "id": "d1a0661e-2339-4dcc-8a87-9a7ffe0e3731",
        "first": "first",
        "last": "last",
        "email": "email",
        "role": "default_role",
        "last_login": datetime(2024, 8, 11, 13, 56, 56, 642916),  # noqa: DTZ001 TODO(MaxGonchar): remove when add tz to db model
        "psw": "password",
    }

    user = User(
        id=expected_user["id"],
        first=expected_user["first"],
        last=expected_user["last"],
        email=expected_user["email"],
        role=expected_user["role"],
        last_login=expected_user["last_login"],
    )
    user.hash_psw(expected_user["psw"])

    with app.app_context():
        subj.add_user(user)

    db_users = get_db_user(expected_user["email"])

    assert len(db_users) == 1, "User not added to db"
    db_user = db_users[0]
    assert_user(expected_user, db_user)
