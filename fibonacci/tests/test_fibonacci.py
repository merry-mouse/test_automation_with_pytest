import json

import pytest
from django.test import Client

fibonacci_url = "http://127.0.0.1:8000/fibonacci"


@pytest.mark.parametrize("param,number", [(1, 1), (2, 1), (5, 5), (20, 6765)])
def test_fibonacci_view_ok(param: int, number: int, client: Client):
    response = client.get(path=fibonacci_url + f"?n={param}")
    assert response.status_code == 200
    data = json.loads(response.content)
    assert data["fibonacci"] == number


@pytest.mark.parametrize("param", [15.5, -1, "a", ""])
def test_fibonacci_bad_response_to_bad_params(param, client: Client):
    response = client.get(path=fibonacci_url + f"?n={param}")
    assert response.status_code == 400
    data = json.loads(response.content)
    assert data["error"] == "query number must be a positive integer or 0"
