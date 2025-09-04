def test_api_add():
    from fastapi.testclient import TestClient
    from hello import app

    client = TestClient(app)

    response = client.get("/add/2/3")
    assert response.status_code == 200
    assert response.json() == {"result": 5}

    response = client.get("/add/-1/1")
    assert response.status_code == 200
    assert response.json() == {"result": 0}

    response = client.get("/add/0/0")
    assert response.status_code == 200
    assert response.json() == {"result": 0}

    response = client.get("/add/-2/-3")
    assert response.status_code == 200
    assert response.json() == {"result": -5}