from fastapi.testclient import TestClient
from companypolic.main import app

client = TestClient(app)


def test_answers_and_refuses():
    hit = client.post("/ask", json={"question": 'Why do production deploys refuse latest tags?'}).json()
    assert hit["answered"] is True
    assert hit["citation"] == "policy.md"
    miss = client.post("/ask", json={"question": 'orbital mechanics homework'}).json()
    assert miss["answered"] is False


def test_empty_is_refused():
    assert client.post("/ask", json={"question": " "}).status_code == 422
