import pytest
import httpx

@pytest.fixture(scope="module")
def client():
    return httpx.Client(base_url="http://localhost:8000")

def test_add(client):
    response = client.get("/add", params={"a": 1, "b": 2})
    assert response.json() == {"result": 3}

    response = client.get("/add", params={"a": 3, "b": 4})
    assert response.json() == {"result": 7}

def test_subtract(client):
    response = client.get("/subtract", params={"a": 1, "b": 2})
    assert response.json() == {"result": -1}

    response = client.get("/subtract", params={"a": 3, "b": 4})
    assert response.json() == {"result": -1}

def test_multiply(client):
    response = client.get("/multiply", params={"a": 1, "b": 2})
    assert response.json() == {"result": 2}

    response = client.get("/multiply", params={"a": 3, "b": 4})
    assert response.json() == {"result": 12}

def test_divide(client):
    response = client.get("/divide", params={"a": 1, "b": 2})
    assert response.json() == {"result": 0.5}

    response = client.get("/divide", params={"a": 3, "b": 4})
    assert response.json() == {"result": 0.75}

def test_divide_exception(client):
    response = client.get("/divide", params={"a": 1, "b": 0})
    assert response.status_code == 400
    assert response.json() == {"detail": "Can't divide by zero"}