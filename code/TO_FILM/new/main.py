# pylint: disable-all

import requests

def get_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"

    try:
        response = requests.get(url)
        data = response.json()
        return data["bpi"]["USD"]["rate"]
    except Exception: 
        print("Error parsing Bitcoin price data.")
        return None

print(f"Current Bitcoin price: ${get_bitcoin_price()}")
