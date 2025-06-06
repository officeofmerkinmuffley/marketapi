import requests
import os
from dotenv import load_dotenv

load_dotenv()
POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")

symbol = "GME"
url = f"https://api.polygon.io/v2/last/trade/stocks/{symbol}?apiKey={POLYGON_API_KEY}"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print(f"[{symbol}] Price: {data['results']['p']} | Time: {data['results']['t']}")
except Exception as e:
    print("Error:", e)
