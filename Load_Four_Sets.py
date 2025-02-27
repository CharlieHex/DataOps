import os
import time
import pandas as pd
from pyspark.sql import SparkSession

print("Starting SparkSession...")

# Start Spark session and connect to Spark Master inside Docker
spark = SparkSession.builder \
    .appName("FootballDataProcessing") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

print("SparkSession started successfully!")

# Define file paths inside Docker
file_paths = [
    "/data/former_names.csv",
    "/data/goalscorers.csv",
    "/data/results.csv",
    "/data/shootouts.csv"
]

print("\nReading File Paths:")

# Check if files exist before loading
for path in file_paths:
    if not os.path.exists(path):
        print(f"Error: File {path} not found!")

# Load datasets
df1 = spark.read.csv(file_paths[0], header=True, inferSchema=True)
df2 = spark.read.csv(file_paths[1], header=True, inferSchema=True)
df3 = spark.read.csv(file_paths[2], header=True, inferSchema=True)
df4 = spark.read.csv(file_paths[3], header=True, inferSchema=True)

# Show schema
df1.printSchema()
df2.printSchema()
df3.printSchema()
df4.printSchema()
