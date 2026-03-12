from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login():
    response = client.post(
        "/auth/login",
        json={
            "email": "user1@email.com",
            "password": "12345"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data


def test_rota_protegida():

    login = client.post(
        "/auth/login",
        json={
            "email": "user1@email.com",
            "password": "12345"
        }
    )

    token = login.json()["access_token"]

    response = client.get(
        "/imoveis/",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    

    assert response.status_code == 200