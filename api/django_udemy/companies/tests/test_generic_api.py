import json

import pytest
import requests


@pytest.mark.crypto
def test_doge_api():
    response = requests.get(url="https://api.coinlore.net/api/ticker?id=90")

    response_content = json.loads(response.content)
    assert response.status_code == 200
    assert response_content[0]["id"] == "90"
    assert response_content[0]["name"] == "Bitcoin"
