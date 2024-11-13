# Use the official Spark image from Docker Hub
FROM bitnami/spark:latest

# Set environment variables for Spark
ENV SPARK_HOME=/opt/bitnami/spark
ENV SPARK_MASTER_URL=spark://spark-master:7077
ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3

# Install Python packages (PySpark connector for Cassandra)
RUN pip install pyspark cassandra-driver

# Set the working directory
WORKDIR /workspace

# Copy your Python script into the container
COPY . /workspace

# Command to run Spark
CMD ["spark-submit", "--master", "spark://spark-master:7077", "script/spark_cassandra_loader.py"]
