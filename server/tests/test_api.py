from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_create_tweet():
    response = client.post("/api/tweets", json={"content": "Hello world!", "api_key": "valid_api_key"})
    assert response.status_code == 200
    assert response.json()["result"] == True
