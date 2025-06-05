import os
import requests
import time

# Load API keys from environment
API_KEY = os.getenvPKZVNC6QQMGCTLCBIKKB
API_SECRET = os.getenv6ebIz1DxHXNvr8U3Tcw9CCcxDbkRdkp7rE6ioMIk

HEADERS = {
        "APCA-API-KEY-ID": PKZVNC6QQMGCTLCBIKKB,
    "APCA-API-SECRET-KEY": 6ebIz1DxHXNvr8U3Tcw9CCcxDbkRdkp7rE6ioMIk
}

SYMBOLS = ["BTC/USD", "GME/USD", "BITO/USD"]

BASE_URL = "https://data.alpaca.markets/v1beta1/crypto/latest/bars"

def fetch_latest_bars():
    symbol_list = ",".join(SYMBOLS)
    url = f"{BASE_URL}?symbols={symbol_list}"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json().get("bars", {})

        for symbol in SYMBOLS:
            bar = data.get(symbol)
            if bar:
                print(f"[{symbol}] Price: {bar['c']} | Volume: {bar['v']} | Time: {bar['t']}")
            else:
                print(f"[{symbol}] No data returned.")

    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")

if __name__ == "__main__":
    while True:
        fetch_latest_bars()
        time.sleep(30)  # Poll every 30 seconds
