import requests
import time
import os

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")


print("🚀 Script started")

if not POLYGON_API_KEY:
    print("❌ POLYGON_API_KEY is not set")
else:
    print("✅ POLYGON_API_KEY is loaded")

# Symbols
CRYPTO_SYMBOLS = [("BTC", "USD")]
STOCK_SYMBOLS = ["AAPL", "TSLA"]

# URL templates
STOCK_URL_TEMPLATE = "https://api.polygon.io/v2/last/trade/stocks/{symbol}"
CRYPTO_URL_TEMPLATE = "https://api.polygon.io/v2/last/trade/crypto/{from_curr}/{to_curr}"

def fetch_crypto_prices():
    for from_curr, to_curr in CRYPTO_SYMBOLS:
        url = CRYPTO_URL_TEMPLATE.format(from_curr=from_curr, to_curr=to_curr)
        params = {"apiKey": POLYGON_API_KEY}
        print(f"📡 [CRYPTO] Calling: {url}")
        try:
            response = requests.get(url, params=params)
            print(f"🔍 [CRYPTO] Status: {response.status_code}")
            print(f"🧾 [CRYPTO] Response Text: {response.text}")
            response.raise_for_status()
            data = response.json().get("data", {})
            print(f"[Crypto {from_curr}-{to_curr}] Price: {data.get('p')} | Size: {data.get('s')} | Time: {data.get('t')}")
        except Exception as e:
            print(f"❌ Crypto API Error for {from_curr}-{to_curr}: {e}")


def fetch_stock_prices():
    for symbol in STOCK_SYMBOLS:
        url = STOCK_URL_TEMPLATE.format(symbol=symbol)
        params = {"apiKey": POLYGON_API_KEY}
        print(f"📡 [STOCK] Calling: {url}")
        try:
            response = requests.get(url, params=params)
            print(f"🔍 [STOCK] Status: {response.status_code}")
            print(f"🧾 [STOCK] Response Text: {response.text}")
            response.raise_for_status()
            data = response.json().get("results", {})
            print(f"[Stock {symbol}] Price: {data.get('p')} | Size: {data.get('s')} | Time: {data.get('t')}")
        except Exception as e:
            print(f"❌ Stock API Error for {symbol}: {e}")


if __name__ == "__main__":
    print("📡 Entering polling loop...")
    loop_counter = 0

    while True:
        try:
            print(f"\n🔁 Poll #{loop_counter}")
            fetch_crypto_prices()
            fetch_stock_prices()
            loop_counter += 1
        except Exception as e:
            print(f"💥 Loop crashed: {e}")

        time.sleep(30)
