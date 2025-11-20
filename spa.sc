# Step 1: Import required modules
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import avg, col

# Step 2: Initialize Spark Session
spark = SparkSession.builder \
    .appName("StockMovingAverage") \
    .getOrCreate()

# Step 3: Read stock market dataset into DataFrame
# Make sure the CSV file has columns: Date, StockSymbol, ClosePrice
df = spark.read.csv("stock_data.csv", header=True, inferSchema=True)

# Step 4: Display first 5 rows to check data
print("Original Data:")
df.show(5)

# Step 5: Define window specification
# Partition by StockSymbol, order by Date, 3-day moving window (current + previous 2 rows)
windowSpec = Window.partitionBy("StockSymbol").orderBy("Date").rowsBetween(-2, 0)

# Step 6: Calculate moving average of ClosePrice
df = df.withColumn("MovingAverage", avg(col("ClosePrice")).over(windowSpec))

# Step 7: Show top 10 rows of the result
print("Top 10 rows with Moving Average:")
df.show(10)

# Step 8: Stop Spark session
spark.stop()

pip install pyspark
python moving_average.py
