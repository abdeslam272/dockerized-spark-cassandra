version: '3'

services:
  spark-master:
    image: bitnami/spark:latest
    container_name: spark-master
    environment:
      - SPARK_MODE=master
    ports:
      - "8080:8080"  # Spark UI
      - "7077:7077"  # Spark master port
    volumes:
      - ./workspace:/workspace  # Mount the current directory into the container
    networks:
      - spark-network

  spark-worker:
    image: bitnami/spark:latest
    container_name: spark-worker
    environment:
      - SPARK_MODE=worker
      - SPARK_MASTER=spark://spark-master:7077
    depends_on:
      - spark-master
    networks:
      - spark-network

  cassandra:
    image: cassandra:latest
    container_name: cassandra
    environment:
      - CASSANDRA_CLUSTER_NAME=SparkCassandraCluster
      - CASSANDRA_LISTEN_ADDRESS=cassandra
      - CASSANDRA_RPC_ADDRESS=0.0.0.0
      - CASSANDRA_BROADCAST_ADDRESS=cassandra
      - CASSANDRA_BROADCAST_RPC_ADDRESS=cassandra
    ports:
      - "9042:9042"  # Cassandra port
    volumes:
      - cassandra-data:/var/lib/cassandra
    networks:
      - spark-network

volumes:
  cassandra-data:

networks:
  spark-network:
    driver: bridge
