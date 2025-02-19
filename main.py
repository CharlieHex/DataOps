from pyspark.sql import SparkSession


# Start Spark session (Single Master, no Workers)
spark = SparkSession.builder \
.appName("FootballDataProcessing") \
.master("local[*]") \
.getOrCreate()

# Load all four datasets
df1 = spark.read.csv(".\\Football_Results\\former_names.csv", header=True, inferSchema=True)
df2 = spark.read.csv(".\\Football_Results\\goalscorers.csv", header=True, inferSchema=True)
df3 = spark.read.csv(".\\Football_Results\\results.csv", header=True, inferSchema=True)
df4 = spark.read.csv(".\\Football_Results\\shootouts.csv", header=True, inferSchema=True)

# Show schema and data of each dataset
df1.printSchema()
df1.show()
df2.printSchema()
df2.show()
df3.printSchema()
df3.show()
df4.printSchema()
df4.show()