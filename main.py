import requests

BOT_TOKEN = "7582265292:AAFAfiID2EjDbju20dtvLx5CJR-kCeyAm1s"
USER_ID = 2075109889
MESSAGE = "Test alert: Telegram bot push notifications are working."

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": USER_ID,
    "text": MESSAGE
}

response = requests.post(url, data=payload)

print(response.status_code)
print(response.text)


import os
import requests
import time

API_KEY = os.getenv("APCA_API_KEY")
API_SECRET = os.getenv("APCA_API_SECRET")

HEADERS = {
    "APCA-API-KEY-ID": getenvPKZVNC6QQMGCTLCBIKKB
    "APCA-API-SECRET-KEY": getenv6ebIz1DxHXNvr8U3Tcw9CCcxDbkRdkp7rE6ioMIk
}

CRYPTO_SYMBOLS = ["BTC/USD"]
STOCK_SYMBOLS = ["GME", "BITO"]

CRYPTO_URL = "https://data.alpaca.markets/v1beta1/crypto/latest/bars"
STOCK_URL_TEMPLATE = "https://data.alpaca.markets/v2/stocks/{}/quotes/latest"

def fetch_crypto_bars():
    url = f"{CRYPTO_URL}?symbols={','.join(CRYPTO_SYMBOLS)}"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json().get("bars", {})
        for symbol in CRYPTO_SYMBOLS:
            bar = data.get(symbol)
            if bar:
                print(f"[{symbol}] Price: {bar['c']} | Volume: {bar['v']} | Time: {bar['t']}")
            else:
                print(f"[{symbol}] No data returned.")
    except requests.exceptions.RequestException as e:
        print(f"Crypto API Error: {e}")

def fetch_stock_quotes():
    for symbol in STOCK_SYMBOLS:
        url = STOCK_URL_TEMPLATE.format(symbol)
        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            quote = response.json().get("quote", {})
            print(f"[{symbol}] Bid: {quote.get('bp')} | Ask: {quote.get('ap')} | Time: {quote.get('t')}")
        except requests.exceptions.RequestException as e:
            print(f"Stock API Error for {symbol}: {e}")

if __name__ == "__main__":
    while True:
        fetch_crypto_bars()
        fetch_stock_quotes()
        time.sleep(30)
