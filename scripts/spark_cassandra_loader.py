from pyspark.sql import SparkSession

# Initialize the Spark session
spark = SparkSession.builder \
    .appName("CSV to Cassandra") \
    .config("spark.cassandra.connection.host", "cassandra") \
    .config("spark.cassandra.auth.username", "cassandra") \
    .config("spark.cassandra.auth.password", "cassandra") \
    .getOrCreate()

# Load CSV into Spark DataFrame
df = spark.read.csv("path_to_your_file.csv", header=True, inferSchema=True)

# Show the first few rows
df.show()

# Perform any transformation you want here, for example:
df_transformed = df.withColumn("new_column", df["existing_column"] * 10)

# Write the DataFrame to Cassandra
df_transformed.write \
    .format("org.apache.spark.sql.cassandra") \
    .option("keyspace", "your_keyspace") \
    .option("table", "your_table") \
    .mode("append") \
    .save()
