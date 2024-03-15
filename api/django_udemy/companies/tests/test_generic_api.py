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


import responses


@pytest.mark.crypto
@responses.activate
def test_mocked_eth_api():
    responses.add(
        method=responses.GET,
        url="https://api.coinlore.net/api/ticker?id=90",
        json=[
            {
                "id": "80",
                "symbol": "ETH",
                "name": "Ethereum",
                "nameid": "ethereum",
                "rank": 2,
                "price_usd": "3741.85",
                "percent_change_24h": "-5.80",
                "percent_change_1h": "0.13",
                "percent_change_7d": "-3.56",
                "price_btc": "0.054781",
                "market_cap_usd": "457910519079.42",
                "volume24": 29435414900.297123,
                "volume24a": 19413310228.00195,
                "csupply": "122375302.00",
                "tsupply": "122375302",
                "msupply": "",
            }
        ],
        status=200,
    )
    response = requests.get(url="https://api.coinlore.net/api/ticker?id=90")

    response_content = json.loads(response.content)
    assert response.status_code == 200
    assert response_content[0]["id"] == "80"
    assert response_content[0]["name"] == "Ethereum"
