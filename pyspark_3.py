from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("FootballDataProcessing") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

print(spark.version)  # To check if the Spark session is correctly initialized