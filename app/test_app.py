import pytest
from app import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200


def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200


def test_liveness(client):
    response = client.get('/live')
    assert response.status_code == 200


def test_readiness_not_ready(client):
    response = client.get('/ready')
    assert response.status_code == 503
