from pyspark.sql import SparkSession

# Initialize the Spark session
spark = SparkSession.builder \
    .appName("Test Spark Session") \
    .config("spark.cassandra.connection.host", "cassandra") \
    .config("spark.cassandra.auth.username", "cassandra") \
    .config("spark.cassandra.auth.password", "cassandra") \
    .getOrCreate()

# Test Spark session by displaying Spark version
print("Spark version:", spark.version)

# Create a simple DataFrame and show it
df = spark.createDataFrame([("Alice", 34), ("Bob", 45), ("Charlie", 23)], ["name", "age"])
df.show()

# Save the simple DataFrame to Cassandra (use a known keyspace and table)
df.write \
    .format("org.apache.spark.sql.cassandra") \
    .option("keyspace", "test_keyspace") \
    .option("table", "test_table") \
    .mode("append") \
    .save()

print("Data written to Cassandra.")

# Read data from Cassandra
df_cassandra = spark.read \
    .format("org.apache.spark.sql.cassandra") \
    .option("keyspace", "test_keyspace") \
    .option("table", "test_table") \
    .load()

df_cassandra.show()


spark.stop()
