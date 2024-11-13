from pyspark.sql import SparkSession
import os

# Retrieve Cassandra connection details from environment variables for security and flexibility
cassandra_host = os.getenv("CASSANDRA_HOST", "cassandra")
cassandra_user = os.getenv("CASSANDRA_USER", "cassandra")
cassandra_password = os.getenv("CASSANDRA_PASSWORD", "cassandra")

# Initialize the Spark session with error handling and configurations
try:
    spark = SparkSession.builder \
        .appName("CSV to Cassandra") \
        .config("spark.cassandra.connection.host", cassandra_host) \
        .config("spark.cassandra.auth.username", cassandra_user) \
        .config("spark.cassandra.auth.password", cassandra_password) \
        .config("spark.sql.shuffle.partitions", "200") \
        .getOrCreate()

    print("Spark session initialized successfully.")
except Exception as e:
    print(f"Error initializing Spark session: {e}")
    raise

# Load CSV into Spark DataFrame, assuming file is present at the specified location
csv_path = "data/Superstore.csv"
try:
    df = spark.read.csv(csv_path, header=True, inferSchema=True)
    print(f"CSV loaded successfully from {csv_path}")
    df.show()
except Exception as e:
    print(f"Error loading CSV file: {e}")
    raise

# Perform any transformation you want here
df_transformed = df  # In this case, no transformation, but you can add your own.

# Write the DataFrame to Cassandra
try:
    df_transformed.write \
        .format("org.apache.spark.sql.cassandra") \
        .option("keyspace", "my_keyspace") \
        .option("table", "my_table") \
        .mode("append") \
        .save()
    print("Data written to Cassandra successfully.")
except Exception as e:
    print(f"Error writing data to Cassandra: {e}")
    raise
