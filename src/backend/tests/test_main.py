"""
Test file
"""

import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def test_app():
    """
    app fixture
    """
    client = TestClient(app)
    yield client


def test_index(test_app):  # pylint: disable=W0621
    """
    test / route
    """
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"ok": True}
