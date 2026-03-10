import json
import time
import requests
from kafka import KafkaProducer

API_KEY = "UU3AHYQTACO133W1"
SYMBOL = "TSLA"
TOPIC = "market-trend"

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

url = "https://www.alphavantage.co/query"

while True:
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": SYMBOL,
        "apikey": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    quote = data.get("Global Quote", {})

    if quote:
        message = {
            "symbol": quote.get("01. symbol"),
            "price": quote.get("05. price"),
            "change": quote.get("09. change"),
            "change_percent": quote.get("10. change percent"),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        producer.send(TOPIC, value=message)
        producer.flush()
        print("Sent to Kafka:", message)
    else:
        print("No data received:", data)

    time.sleep(60)