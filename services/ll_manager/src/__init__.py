import os

from flask import Response, jsonify
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_openapi3 import OpenAPI  # type: ignore [import-untyped]

from src.api.auth import auth_api
from src.extensions import db

# for alembic
from src.models import User

#TODO: add /api to all routes
app = OpenAPI(__name__)
app.config.from_object("src.config.Config")

db.init_app(app)
Migrate(app, db, directory=os.path.join("src", "migrations"))
jwt = JWTManager(app)

app.register_api(auth_api)

# TODO: remove this route
@app.get("/")
def hello_world() -> Response:
    return jsonify(hello="world!!!")


@app.get("/health")
def health() -> Response:
    return jsonify(status="ok")
