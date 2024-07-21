import pytest
from flask.testing import FlaskClient

from src import app


@pytest.fixture()
def test_client() -> FlaskClient:
    return app.test_client()
