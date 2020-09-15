import pytest
from ...app import create_app


BASE_ROUTE = '/hello-world'


@pytest.fixture
def app():
    app = create_app()
    return app


def test_hello_world(client):
    response = client.get(BASE_ROUTE)
    assert response.status_code == 200
    assert response.json == 'Hello World'