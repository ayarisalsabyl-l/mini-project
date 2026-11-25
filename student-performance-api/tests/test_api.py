from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == (
        "Student Performance API is running"
    )

def test_predict():
    response = client.post(
        "/predict",
        json={
            "study_hours": 6,
            "attendance": 85,
            "previous_score": 72,
            "assignments_completed": 8
        }
    )
    assert response.status_code == 200
    assert response.json()["result"] == "Pass