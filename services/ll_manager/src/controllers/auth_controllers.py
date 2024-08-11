from uuid import uuid4
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import datetime

import src.repos.auth_repo as repo
from src.schema.auth import SignOnRequest, SignOnResponse
from src.models.user import User


def get_current_time():
    return datetime.now()


def register(user: SignOnRequest) -> str:
    user_id = uuid4()
    user_to_add = User(
        id=user_id,
        first=user.first,
        last=user.last,
        email=user.email,
        role="default_role",
        last_login=get_current_time(),
    )
    user_to_add.hash_psw(user.psw)
    repo.add_user(user_to_add)
    return SignOnResponse(
        access_token=create_access_token(identity=user_id),
        refresh_token=create_refresh_token(identity=user_id),
    ).model_dump_json()
