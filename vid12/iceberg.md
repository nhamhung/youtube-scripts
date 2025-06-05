# Overview

1. What is Apache Iceberg?
2. What is Minio
3. Set up Spark + Iceberg with Docker Compose
4. Try out Iceberg features in Jupyter Notebook

# 1. What is Apache Iceberg?

- Table format to provide analytical functionalities for massive raw data tables in data lakes -> modern lakehouse architecture

- Metadata layer on top of raw data to convert it into structured, high-performance "table" for sophisticated analytical applications

### Key features

- **ACID transactions** Atomicity, Consistency, Isolation, Durability to support concurrent read / write and ensure data integrity

- **Schema evolution** without data rewrites or breaking existing queries

- **Time travel** and **rollback** through snapshots

- **Hidden partitioning** to manage it automatically without user's efforts and data rewrites

- **Advanced metadata management** for performance optimisation through manifest files, manifest list, metadata files

- **Multi-engine compatibility** to be vendor-agnostic

# 2. What is MinIO?

- High-performance object storage server that is API-compatible with Amazon S3

- Own private cloud storage that works just like Amazon S3 and can run on own hardware (on-premise)

### Key features

- **Amazon S3 API Compatibility** to seamlessly work with applications designed for S3 without any code change

- **Distributed Object Storage** to scale horizontally across nodes for high availability and tolerance, ideal for unstructured data

- **High Performance** to be suitable for modern AI/ML applications

- **Cloud and Kubernetes Native** to be suitable for containerised environment

# 3. Set up Spark + Iceberg with Docker Compose

- Prepare `docker-compose.yml` file

```
# Start Docker Desktop
docker compose up

# Access MinIO
http://localhost:9001

# Access demo Jupyter Notebook
http://localhost:8888

# Check out Spark-Iceberg container
docker exec -it spark-iceberg bash

# Find jupyter-notebook process
ps aux | grep jupyter-notebook

# Check notebook directory
ls -lh /home/iceberg/notebooks

# Check /home/iceberg directory
ls -lh /home/iceberg/

# Verify local directories notebooks/ and warehouse/ mounted into Docker
touch /home/iceberg/warehouse/file.txt

# Check spark-defaults.conf for Iceberg configs
cat conf/spark-defaults.conf
```

| Config                             | Value                                                             | Description                                                           |
| ---------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------- |
| spark.sql.extensions               | org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions | Add Iceberg capabilities to Spark SQL                                 |
| spark.sql.catalog.demo             | org.apache.iceberg.spark.SparkCatalog                             | Add a Spark SQL Iceberg catalog called "demo"                         |
| spark.sql.catalog.demo.type        | rest                                                              | "demo" will use a REST-based catalog service to manage table metadata |
| spark.sql.catalog.demo.uri         | http://rest:8181                                                  | catalog service REST endpoint                                         |
| spark.sql.catalog.demo.warehouse   | s3://warehouse/wh/                                                | "demo" tables will be inside this root location                       |
| spark.sql.catalog.demo.s3.endpoint | http://minio:9000                                                 | "demo" can find S3 file system at minIO endpoint                      |
| spark.sql.defaultCatalog           | demo                                                              | "demo" will be Spark default catalog                                  |

# 4. Try out Iceberg features in Jupyter Notebook

- After `nyc.taxis` table creation, check it at `http://localhost:9001`

- View sample metadata file

```
cat ~/youtube/vid12/sample-metadata.json | jq
```

- Open `Iceberg - Getting Started.ipynb` notebook

- To save it, create a copy and save to `notebooks/` directory
