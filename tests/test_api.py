from fastapi.testclient import TestClient
from api.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_metadata():
    response = client.get("/metadata")

    assert response.status_code == 200
    assert response.json()["project"] == (
        "Sistema Inteligente para Renta de Vehículos"
    )


def test_ask_vehiculos_disponibles():
    response = client.post(
        "/ask",
        json={
            "pregunta": "¿Qué vehículos están disponibles?"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["tipo_consulta"] == "vehiculos_disponibles"
    assert "Toyota Corolla" in data["respuesta"]
    assert "Nissan Versa" in data["respuesta"]