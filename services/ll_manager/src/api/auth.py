from http import HTTPStatus

from flask import Response, jsonify
from flask_openapi3 import APIBlueprint, Tag  # type: ignore [import-untyped]

from src.controllers import auth_controllers
from src.schema.auth import SignOnRequest, SignOnResponse

auth_api = APIBlueprint("auth", __name__, url_prefix="/auth")

_tag = Tag(name="Auth")


@auth_api.post(
    "/register",
    tags=[_tag],
    summary="create new profile",
    responses={HTTPStatus.CREATED: SignOnResponse},
)
def register(body: SignOnRequest) -> tuple[str, int]:
    resp = auth_controllers.register(body)
    return resp, 201


@auth_api.post("/log_in")
def log_in() -> Response:
    return jsonify(message="hello, hello again!!!")


@auth_api.post("/refresh")
def refresh() -> Response:
    return jsonify(message="you are so fresh now, mmm...")
