import src.repos.auth_repo as repo
from src.schema.auth import SignOnResponse


def sign_on(user):
    repo.add_user(user)
    return SignOnResponse(
        access_token="ACCESS TOKEN",
        refresh_token="REFRESH TOKEN"
    )
