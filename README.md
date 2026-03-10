📈 Real-Time Stock Market Trend Analysis Pipeline




🚀 Project Overview

This project implements a real-time big data pipeline that analyzes stock market event trends using distributed data processing technologies. The system ingests streaming data, processes it with Apache Spark Streaming, stores the results in Hive, and visualizes insights using Grafana dashboards.

The goal of this project is to demonstrate how modern big data technologies can be used together to monitor market activity, detect spikes, and analyze trends over time.

🏗 System Architecture

The pipeline follows a stream processing architecture.

        Data Source
            │
            ▼
       Apache Kafka
      (Streaming Events)
            │
            ▼
      Apache Spark
    (Streaming Processing)
            │
            ▼
         Apache Hive
      (Structured Storage)
            │
            ▼
          Grafana
      (Visualization)



Component Roles

Apache Kafka
Serves as the real-time message broker.
Handles streaming event ingestion.

Apache Spark Streaming
Consumes Kafka events.
Performs window-based aggregation.
Processes streaming data in real time.

Apache Hive
Stores processed results in Parquet format.
Enables structured querying and analysis.

Grafana
Visualizes processed data using dashboards.
Displays market activity trends.



TECHNOLOGIES USED

| Technology             | Purpose                           |
| ---------------------- | --------------------------------- |
| Apache Kafka           | Real-time data streaming          |
| Apache Zookeeper       | Kafka coordination                |
| Apache Spark (PySpark) | Stream processing                 |
| Apache Hive            | Data storage                      |
| HDFS                   | Distributed storage               |
| Grafana                | Data visualization                |
| Python                 | Streaming pipeline implementation |




📊 Dashboard Visualizations

The Grafana dashboard includes several analytical panels.

🔹 Peak Stock Market Event Count
Displays the maximum number of events detected within a processing window, highlighting peak market activity.

🔹 Event Count per Time Window
Shows event counts for each streaming window, helping identify spikes.

🔹 Market Trend Analysis Table
Displays processed output including:

Window start
Window end
Stock symbol
Event count

🔹 Stock Event Count by Symbol
Bar chart comparing event counts across time windows.

🔹 Stock Market Event Count Over Time
Time-series chart showing how market activity changes over time.

🛠 Installation & Setup
1️⃣ Install Required Tools

Install the following components:
Java (JDK 8 or higher)
Apache Kafka
Apache Zookeeper
Apache Spark
Apache Hive
Python
Grafana

2️⃣ Start Services

Start services in the correct order:

Start Zookeeper
Start Kafka
Start Spark
Start Hive

3️⃣ Create Kafka Topic
kafka-topics.sh --create \
--topic stock-events \
--bootstrap-server localhost:9092

4️⃣ Run Streaming Application
Execute the PySpark streaming application.
python streaming_pipeline.py

The application will:
Consume events from Kafka
Process streaming data
Aggregate event counts

5️⃣ Store Results in Hive
Processed data is stored in Hive using Parquet format.

Example schema:

Column	Description
window_start	Aggregation window start
window_end	Aggregation window end
symbol	Stock symbol
count	Event count

6️⃣ Launch Grafana

Start Grafana and access the dashboard:
http://localhost:3000



💡 Key Learnings

This project provided insights into:
Building real-time streaming data pipelines
Implementing window-based aggregations
Integrating multiple big data frameworks
Visualizing streaming analytics dashboards
Managing distributed data processing systems

🔮 Future Improvements

Possible extensions include:
Integration with Alpaca API for real-time stock data
Sentiment analysis using advanced NLP models
Geographic sentiment analysis
Historical vs real-time trend comparison
Machine learning models for market prediction
