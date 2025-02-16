import pandas as pd
from pyspark.sql import SparkSession

# Start Spark session
spark = SparkSession.builder \
.appName("FootballDataProcessing") \
.master("spark://localhost:7077") \
.getOrCreate()

# Load all four datasets
df1 = spark.read.csv("D:\\Git_Folders\\DataOps\\Football_Results\\former_names.csv", header=True, inferSchema=True)
df2 = spark.read.csv("D:\\Git_Folders\\DataOps\\Football_Results\\goalscorers.csv", header=True, inferSchema=True)
df3 = spark.read.csv("D:\\Git_Folders\\DataOps\\Football_Results\\results.csv", header=True, inferSchema=True)
df4 = spark.read.csv("D:\\Git_Folders\\DataOps\\Football_Results\\shootouts.csv", header=True, inferSchema=True)


# Show schema of each dataset
df1.printSchema()
df2.printSchema()
df3.printSchema()
df4.printSchema()
