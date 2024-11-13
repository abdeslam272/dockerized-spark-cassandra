# dockerized-spark-cassandra

# Spark and Cassandra Data Pipeline

This project demonstrates a data pipeline using **Apache Spark** and **Apache Cassandra**. It is containerized with **Docker** and **Docker Compose** to make it easy to deploy and run. The pipeline reads a CSV file, processes it using Spark, and writes the transformed data to a Cassandra database.

## Project Structure

- **Dockerfile**: Defines a custom Docker image for Spark, which installs necessary Python packages and configures Spark for interaction with Cassandra.
- **docker-compose.yml**: Configures and orchestrates containers for Spark Master, Spark Worker, and Cassandra using Docker Compose.
- **scripts/spark_cassandra_loader.py**: A Python script that loads a CSV file into a Spark DataFrame, performs transformations, and writes the result to a Cassandra table.

## Components

### Docker Containers
- **Spark Master**: Manages the Spark cluster.
- **Spark Worker**: Performs distributed data processing.
- **Cassandra**: A NoSQL database that stores the transformed data.

### Python Script
The Python script (`scripts/spark_cassandra_loader.py`) performs the following steps:
1. Initializes a Spark session.
2. Reads a CSV file (`data/Superstore.csv`) into a Spark DataFrame.
3. (Optional) Transforms the DataFrame (e.g., adding or modifying columns).
4. Writes the transformed data to a specified table in the Cassandra database.

## Usage

### Prerequisites
- **Docker** and **Docker Compose** installed on your system.

### Steps to Run
1. Place your CSV file in the `data/` directory with the name `Superstore.csv`.
2. Build and start the Docker containers:
   ```bash
   docker-compose up
3. The Spark job will automatically run, processing the CSV file and storing the data in Cassandra.
