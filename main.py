import websocket
import json
import threading
import os

API_KEY = os.getenv("API_KEY")
TICKERS = ["GME", "MP", "BITO"]

def on_message(ws, message):
    data = json.loads(message)
    for item in data:
        if item.get('ev') == 'T':  # Trade event
            print(f"[{item['sym']}] Price: {item['p']} | Size: {item['s']} | Timestamp: {item['t']}")

def on_error(ws, error):
    print(f"WebSocket Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("WebSocket Closed")

def on_open(ws):
    ws.send(json.dumps({"action": "auth", "params": API_KEY}))
    for ticker in TICKERS:
        ws.send(json.dumps({"action": "subscribe", "params": f"T.{ticker}"}))
print(f"Using API_KEY: {API_KEY}")

def run_ws():
    socket = "wss://socket.polygon.io/stocks"
    ws = websocket.WebSocketApp(socket,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()

if __name__ == "__main__":
    thread = threading.Thread(target=run_ws)
    thread.start()
