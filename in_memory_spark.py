from pyspark.sql import SparkSession
from pyspark.sql.functions import col, mean, round as spark_round
import time

# ---------- Start Spark Session ----------
spark = SparkSession.builder \
    .appName("InMemoryDataProcessing") \
    .getOrCreate()

# ---------- Initial dataset ----------
data = [
    {"sensor":"S1","temp":25.3,"hum":60.2},
    {"sensor":"S2","temp":28.7,"hum":58.7},
    {"sensor":"S3","temp":29.8,"hum":59.6}
]

df = spark.createDataFrame(data)

# ---------- Function to compute averages ----------
def compute_avg(df):
    avg_temp = df.select(spark_round(mean(col("temp")),2)).collect()[0][0]
    avg_hum = df.select(spark_round(mean(col("hum")),2)).collect()[0][0]
    return avg_temp, avg_hum

# ---------- Before caching ----------
start = time.time()
avg_temp, avg_hum = compute_avg(df)
end = time.time()
print(f"Before caching -> Avg Temp: {avg_temp}, Avg Hum: {avg_hum}, Time: {round(end-start,3)}s")

# ---------- Simulate insert/update/delete ----------
# Insert
new_row = [{"sensor":"S4","temp":26.5,"hum":61.0}]
df = df.union(spark.createDataFrame(new_row))

# Update (change S1 temp to 26.0)
df = df.withColumn("temp", 
                   when(col("sensor")=="S1", 26.0).otherwise(col("temp")))

# Delete (remove S2)
df = df.filter(col("sensor") != "S2")

# ---------- After caching ----------
start = time.time()
avg_temp, avg_hum = compute_avg(df)
end = time.time()
print(f"After caching -> Avg Temp: {avg_temp}, Avg Hum: {avg_hum}, Time: {round(end-start,3)}s")

# ---------- Show final dataset ----------
df.show()

# Stop Spark session
spark.stop()
