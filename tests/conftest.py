import pytest
from starlette.testclient import TestClient

from momo.asgi import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  # testing happens here
