import pytest
from main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    client = app.test_client()
    yield client

def test_upload(client):
    with open("test_image.png", "rb") as img:
        response = client.post("/upload", data={"image": img})
        assert response.status_code == 200
        assert "image_id" in response.json

def test_list_objects(client):
    response = client.get("/objects/<valid_image_id>")
    assert response.status_code == 200

def test_object_details(client):
    response = client.get("/objects/<valid_image_id>/<valid_object_id>")
    assert response.status_code == 200
