from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

data = [
    {"window_start": "2026-03-08 19:40:00", "window_end": "2026-03-08 19:41:00", "symbol": "AAPL", "count": 1},
    {"window_start": "2026-03-08 19:41:00", "window_end": "2026-03-08 19:42:00", "symbol": "AAPL", "count": 1},
    {"window_start": "2026-03-08 19:42:00", "window_end": "2026-03-08 19:43:00", "symbol": "AAPL", "count": 1},
    {"window_start": "2026-03-08 19:43:00", "window_end": "2026-03-08 19:44:00", "symbol": "AAPL", "count": 1},
    {"window_start": "2026-03-08 19:44:00", "window_end": "2026-03-08 19:45:00", "symbol": "AAPL", "count": 8},
    {"window_start": "2026-03-08 19:46:00", "window_end": "2026-03-08 19:47:00", "symbol": "AAPL", "count": 12},
    {"window_start": "2026-03-08 19:47:00", "window_end": "2026-03-08 19:48:00", "symbol": "AAPL", "count": 1}
]

for row in data:
    producer.send("market-trend-analysis", value=row)
    print("Sent:", row)

producer.flush()
producer.close()
print("All analyzed rows sent to Kafka topic: market-trend-analysis")