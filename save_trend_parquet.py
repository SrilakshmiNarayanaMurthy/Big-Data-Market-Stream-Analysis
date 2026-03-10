import pandas as pd

data = [
    {"window_start": "2026-03-08 19:40:00", "window_end": "2026-03-08 19:41:00", "symbol": "AAPL", "count": 1},
    {"window_start": "2026-03-08 19:41:00", "window_end": "2026-03-08 19:42:00", "symbol": "AAPL", "count": 1},
    {"window_start": "2026-03-08 19:42:00", "window_end": "2026-03-08 19:43:00", "symbol": "AAPL", "count": 1},
    {"window_start": "2026-03-08 19:43:00", "window_end": "2026-03-08 19:44:00", "symbol": "AAPL", "count": 1},
    {"window_start": "2026-03-08 19:44:00", "window_end": "2026-03-08 19:45:00", "symbol": "AAPL", "count": 8},
    {"window_start": "2026-03-08 19:46:00", "window_end": "2026-03-08 19:47:00", "symbol": "AAPL", "count": 12},
    {"window_start": "2026-03-08 19:47:00", "window_end": "2026-03-08 19:48:00", "symbol": "AAPL", "count": 1}
]

df = pd.DataFrame(data)

# keep as strings so Spark can read safely
df["window_start"] = df["window_start"].astype(str)
df["window_end"] = df["window_end"].astype(str)

df.to_parquet("market_trend_output.parquet", index=False)

print("Parquet file saved as market_trend_output.parquet")
print(df)