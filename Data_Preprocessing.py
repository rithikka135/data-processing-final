from pyspark.sql import SparkSession
from pyspark.sql.functions import col, mean, when, round as spark_round

# Start Spark session
spark = SparkSession.builder.appName("SensorDataPreprocessing").getOrCreate()

# Load sample data
data = [
    ("S1", 25.3, 60.2, 1013, "ON", "2025-10-16 08:00:00"),
    ("S2", None, 58.7, 1011, "OFF", "2025-10-16 08:01:00"),
    ("S3", 29.8, None, 1012, "ON", "2025-10-16 08:02:00"),
    ("S1", 25.3, 60.2, 1013, "ON", "2025-10-16 08:00:00")  # Duplicate
]

columns = ["sensor_id", "temperature", "humidity", "pressure", "status", "timestamp"]
df = spark.createDataFrame(data, columns)

# Handle missing values with mean
avg_temp = df.select(mean(col("temperature"))).collect()[0][0]
avg_hum = df.select(mean(col("humidity"))).collect()[0][0]
df = df.withColumn("temperature", when(col("temperature").isNull(), avg_temp).otherwise(col("temperature")))
df = df.withColumn("humidity", when(col("humidity").isNull(), avg_hum).otherwise(col("humidity")))

# Remove duplicates
df = df.dropDuplicates()

# Normalize temperature & humidity
df = df.withColumn("temperature_norm", spark_round(col("temperature") / 100, 2))
df = df.withColumn("humidity_norm", spark_round(col("humidity") / 100, 2))

# Feature engineering: Temp/Humidity ratio
df = df.withColumn("temp_hum_ratio", spark_round(col("temperature") / col("humidity"), 2))

# Show final preprocessed data
df.show()
