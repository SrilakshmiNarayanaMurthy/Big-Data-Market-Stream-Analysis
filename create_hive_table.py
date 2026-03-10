from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("CreateHiveExternalTable") \
    .config("spark.sql.warehouse.dir", "file:///E:/spark-warehouse") \
    .enableHiveSupport() \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

parquet_folder = "file:///E:/NEW VOLUMEF/DESKTOP/MS 3rd sem/big data/HW2/market_trend_hive_data"

print("=== TEST READ PARQUET FOLDER ===")
df = spark.read.parquet(parquet_folder)
df.show(truncate=False)
df.printSchema()

spark.sql("CREATE DATABASE IF NOT EXISTS market_db")
spark.sql("DROP TABLE IF EXISTS market_db.market_trend_hive")

spark.sql(f"""
CREATE EXTERNAL TABLE market_db.market_trend_hive (
    window_start STRING,
    window_end STRING,
    symbol STRING,
    count BIGINT
)
STORED AS PARQUET
LOCATION '{parquet_folder}'
""")

print("=== DATABASES ===")
spark.sql("SHOW DATABASES").show(truncate=False)

print("=== TABLES IN market_db ===")
spark.sql("SHOW TABLES IN market_db").show(truncate=False)

print("=== HIVE TABLE DATA ===")
spark.sql("SELECT * FROM market_db.market_trend_hive").show(truncate=False)

spark.stop()