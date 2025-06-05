import websocket
import json
import threading
import os

ALPACA_API_KEY = os.getenv("APKZVNC6QQMGCTLCBIKKB")
ALPACA_SECRET_KEY = os.getenv("6ebIz1DxHXNvr8U3Tcw9CCcxDbkRdkp7rE6ioMIk")
BASE_URL = "https://paper-api.alpaca.markets/v2"

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
    auth_payload = {"action": "auth", "params": f"{API_KEY}"}
    print(f"Sending auth: {auth_payload}")
    ws.send(json.dumps(auth_payload))

    for ticker in TICKERS:
        sub_payload = {"action": "subscribe", "params": f"T.{ticker}"}
        print(f"Subscribing to: {sub_payload}")
        ws.send(json.dumps(sub_payload))



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
