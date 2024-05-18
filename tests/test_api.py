import pytest
from src.main import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    with app.test_client() as client:
        yield client


def test_status(client):
    response = client.get("/status")
    assert response.status_code == 200
    assert b"System is operational" in response.data


def test_summary(client):
    response = client.post("/summary", json={"input_data": "Example data"})
    assert response.status_code == 200
    assert 'summary' in response.json
    assert response.json['summary'] == "Generated summary based on processed data"
