import requests
import time
import os

# Load Polygon API key from environment
POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")

# Define tickers
CRYPTO_SYMBOLS = ["BTC-USD"]
STOCK_SYMBOLS = [
    "GME", "BITO", "MP", "UUUU", "REMX", "IBIT", "HUT", "MARA", "MSTR",
    "DJT", "NXTT", "YGME", "YBITO", "MSTY", "GRYP", "GITS", "BMGL",
    "TSLA", "PLTR", "COIN", "HOOD", "VIXX", "SOFI", "GDX", "VYM",
    "BWEB", "WOLF", "RIOT", "SMLR", "STRK", "XYZ"
]

# Polygon endpoints
CRYPTO_URL_TEMPLATE = "https://api.polygon.io/v1/last/crypto/{symbol}"
STOCK_URL_TEMPLATE = "https://api.polygon.io/v2/last/trade/stocks/{symbol}"

# Function to fetch crypto prices
def fetch_crypto_prices():
    for symbol in CRYPTO_SYMBOLS:
        url = CRYPTO_URL_TEMPLATE.format(symbol=symbol)
        params = {"apiKey": POLYGON_API_KEY}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json().get("last", {})
            print(f"[Crypto {symbol}] Price: {data.get('price')} | Size: {data.get('size')} | Time: {data.get('timestamp')}")
        except requests.exceptions.RequestException as e:
            print(f"Crypto API Error for {symbol}: {e}")

# Function to fetch stock prices
def fetch_stock_prices():
    for symbol in STOCK_SYMBOLS:
        url = STOCK_URL_TEMPLATE.format(symbol=symbol)
        params = {"apiKey": POLYGON_API_KEY}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json().get("results", {})
            print(f"[Stock {symbol}] Price: {data.get('p')} | Size: {data.get('s')} | Time: {data.get('t')}")
        except requests.exceptions.RequestException as e:
            print(f"Stock API Error for {symbol}: {e}")

# Main function to fetch data
if __name__ == "__main__":
    while True:
        fetch_crypto_prices()
        fetch_stock_prices()
        time.sleep(30)  # Poll every 30 seconds
