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

def test_rota_admin():
    # user normal
    login_user = client.post("/auth/login", json={"email": "user1@email.com", "password": "12345"})
    token_user = login_user.json()["access_token"]

    # tentar acessar rota admin
    responser_user = client.get(
        "/admin-only",
        headers={"Authorization": f"bearer {token_user}"}
    )
    assert responser_user.status_code == 403

    # login admin
    login_admin = client.post("/auth/login", json={"email": "admin@email.com", "password": "12345"})
    token_admin = login_admin.json()["access_token"]
    print(token_admin)
    # acessar rota de admin
    responser_admin = client.get(
        "/admin-only",
        headers={"Authorization": f"bearer {token_admin}"}
    )

    assert responser_admin.status_code == 200
