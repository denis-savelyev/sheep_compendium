from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_sheep():
    response = client.get("/sheep/1")

    assert response.status_code == 200

    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

def test_add_sheep():

    test_data = {
        "id": 4,
        "name": "Clover",
        "breed": "Icelandic",
        "sex": "ewe"
    }

    response = client.post("/sheep/", json=test_data)

    assert response.status_code == 201

    assert response.json() == test_data

    assert client.get("/sheep/4").json() == test_data

def test_delete_sheep():
    test_data = {
        "id": 5,
        "name": "Clover",
        "breed": "Icelandic",
        "sex": "ewe"
    }

    response = client.post("/sheep/", json=test_data)

    assert response.status_code == 201

    response = client.delete("/sheep/5")

    assert response.status_code == 204

def test_update_sheep():

    test_data = {
        "id": 5,
        "name": "New Clover",
        "breed": "Norwegian",
        "sex": "ewe"
    }

    response = client.put("/sheep/5", json=test_data)

    assert response.status_code == 204

    assert client.get("/sheep/6").json() == test_data