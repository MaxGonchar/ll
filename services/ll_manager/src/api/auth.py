from http import HTTPStatus

from flask import Response, jsonify
from flask_openapi3 import APIBlueprint, Tag

from src.controllers import auth_controllers
from src.schema.auth import SignOnRequest, SignOnResponse

auth_api = APIBlueprint("/auth", __name__)

_tag = Tag(name="Auth")



@auth_api.post(
        "/register",
        tags=[_tag],
        summary="create new profile",
        responses={HTTPStatus.CREATED: SignOnResponse},
    )
def register(body: SignOnRequest) -> Response:
    resp = auth_controllers.register(body)
    return resp.model_dump_json(), 201


@auth_api.post("/log_in")
def log_in() -> Response:
    return jsonify(message="hello, hello again!!!")


@auth_api.post("/refresh")
def refresh() -> Response:
    return jsonify(message="you are so fresh now, mmm...")
