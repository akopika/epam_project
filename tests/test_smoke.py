import http

from src import app


def test_smoke():
    client = app.test_client()
    response = client.get("/api/smoke")
    assert response.status_code == http.HTTPStatus.OK
