from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("FootballDataProcessing") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

# Print Spark version
print(f"Spark version: {spark.version}")

# Load the CSV file into a DataFrame
df = spark.read.csv('/data/results.csv', header=True, inferSchema=True)

# Show the first few rows of the DataFrame
df.show()

# Print the schema of the DataFrame
df.printSchema()

# Example transformation: filter rows for years > 2000 and select specific columns
df_filtered = df.filter(df['Year'] > 2000).select('Team', 'Year', 'Goals')

# Show the transformed DataFrame
df_filtered.show()

# Optional: Save the filtered data back to disk (e.g., as CSV)
df_filtered.write.csv('/data/filtered_results.csv', header=True)
