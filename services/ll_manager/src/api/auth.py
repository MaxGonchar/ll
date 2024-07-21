from http import HTTPStatus
from datetime import datetime

from flask import Response, jsonify
from flask_openapi3 import APIBlueprint, Tag

from src.schema.auth import SignOnRequest, SignOnResponse
from src.models import User
from src.extensions import db
import src.controllers.auth_controllers as auth_controllers

auth_api = APIBlueprint("/auth", __name__)

_tag = Tag(name="Auth")



@auth_api.post(
        "/sign_on",
        tags=[_tag],
        summary="create new profile",
        responses={HTTPStatus.CREATED: SignOnResponse},
    )
def sign_on(body: SignOnRequest) -> Response:
    resp = auth_controllers.sign_on(body)
    return resp.model_dump_json(), 201


@auth_api.post("/log_in")
def log_in() -> Response:
    return jsonify(message="hello, hello again!!!")


@auth_api.post("/refresh")
def refresh() -> Response:
    return jsonify(message="you are so fresh now, mmm...")
