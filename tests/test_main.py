# tests/test_main.py
import pytest
from app.main import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello from my app!"}

def test_health_check_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 400
    assert response.get_json() == {"status": "ok"}
