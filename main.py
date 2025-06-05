import requests
import time
import os

# Load API keys from environment variables (recommended for security)
API_KEY = os.getenv("APCA_API_KEY")
API_SECRET = os.getenv("APCA_API_SECRET")

HEADERS = {
    "APCA-API-KEY-ID": API_KEY,
    "APCA-API-SECRET-KEY": API_SECRET
}

# Define tickers
CRYPTO_SYMBOLS = ["BTC/USD"]
STOCK_SYMBOLS = [
    "GME", "BITO", "MP", "UUUU", "REMX", "IBIT", "HUT", "MARA", "MSTR",
    "DJT", "NXTT", "YGME", "YBITO", "MSTY", "GRYP", "GITS", "BMGL",
    "TSLA", "PLTR", "COIN", "HOOD"
]

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
        time.sleep(30)  # Poll every 30 seconds
