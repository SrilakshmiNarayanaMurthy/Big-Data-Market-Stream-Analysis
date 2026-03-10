from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, to_timestamp, window
from pyspark.sql.types import StructType, StringType

spark = SparkSession.builder \
    .appName("MarketTrendBatchAnalysis") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

schema = StructType() \
    .add("symbol", StringType()) \
    .add("price", StringType()) \
    .add("change", StringType()) \
    .add("change_percent", StringType()) \
    .add("timestamp", StringType())

kafka_df = spark.read \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "market-trend") \
    .option("startingOffsets", "earliest") \
    .option("endingOffsets", "latest") \
    .load()

json_df = kafka_df.selectExpr("CAST(value AS STRING) as json_value")

parsed_df = json_df.select(
    from_json(col("json_value"), schema).alias("data")
).select("data.*")

final_df = parsed_df.withColumn(
    "event_time",
    to_timestamp(col("timestamp"), "yyyy-MM-dd HH:mm:ss")
)

print("Raw market records:")
final_df.show(truncate=False)

trend_df = final_df.groupBy(
    window(col("event_time"), "1 minute"),
    col("symbol")
).count()

print("Record count trend by minute:")
trend_df.show(truncate=False)

spark.stop()