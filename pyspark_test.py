from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("FootballDataProcessing") \
    .master("spark://b86fca4df6a4:7077") \
    .config("spark.driver.memory", "2g") \
    .config("spark.executor.memory", "2g") \
    .getOrCreate()

print(spark)