import pytest
from fastapi.testclient import TestClient
from main import app
from database import SessionLocal, Subscription

client = TestClient(app)

#Para probar las pruebas utilizar: pytest -v test_api.py

@pytest.fixture(scope="module")
def test_db():
    db = SessionLocal()
    # Crea una suscripción de prueba
    test_subscription = Subscription(
        id = 1,
        user_id=1,
        topic="test_topic",
        email="user@example.com",
        phone="1234567890",
        subscription_date="2024-09-27",
        active="active",
        notification_type="email",
        additional_info="some_info"
    )
    db.add(test_subscription)
    db.commit()
    db.refresh(test_subscription)
    yield db
    db.query(Subscription).filter(Subscription.id == test_subscription.id).delete()  # Eliminar datos de prueba
    db.commit()

def test_create_subscription():
    response = client.post("/subscriptions/", json={
        "user_id": 1,
        "topic": "test_topic",
        "email": "user@example.com",
        "phone": "1234567890",
        "subscription_date": "2024-09-27",
        "active": "active",
        "notification_type": "email",
        "additional_info": "some_info"
    })
    assert response.status_code == 200
    assert "id" in response.json()

def test_read_all_subscriptions():
    response = client.get("/subscriptions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_subscription(test_db):
    response = client.get("/subscriptions/1")  # Cambia el ID según tus datos
    assert response.status_code == 200
    assert response.json()['user_id'] == 1

def test_update_subscription(test_db):
    response = client.put("/subscriptions/1", json={
        "user_id": 1,
        "topic": "updated_topic",
        "email": "updated@example.com",
        "phone": "0987654321",
        "subscription_date": "2024-09-28",
        "active": "inactive",
        "notification_type": "sms",
        "additional_info": "updated_info"
    })
    assert response.status_code == 200
    assert response.json()['topic'] == "updated_topic"

def test_delete_subscription(test_db):
    response = client.delete("/subscriptions/1")  # Cambia el ID según tus datos
    assert response.status_code == 200
    assert response.json()['detail'] == "Subscription deleted"
