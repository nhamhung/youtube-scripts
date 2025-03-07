# Overview

1. Set up GCP CLI
2. Set up a Spark project
3. Test Spark Streaming with Kafka
4. Test Spark Batch with Couchbase
5. Deploy Spark Jar to Cloud Storage
6. Run Spark application to create partitioned data in Cloud Storage (replace Hadoop)
7. Use BigQuery (replace Hive) to read external table in Cloud Storage

# GCP CLI Setup

GCloud CLI: https://cloud.google.com/sdk/docs/install

```
./google-cloud-sdk/install.sh

gcloud init
```

# Kafka Setup

Kafka Docker: https://hub.docker.com/r/apache/kafka

```
docker pull apache/kafka

docker run -d -p 9092:9092 --name broker apache/kafka:latest

./kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test-topic

./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test-topic
```

# Couchbase Setup

Couchbase Docker: https://hub.docker.com/_/couchbase

```
docker pull couchbase

docker run -d --name db -p 8091-8097:8091-8097 -p 9123:9123 -p 11207:11207 -p 11210:11210 -p 11280:11280 -p 18091-18097:18091-18097 couchbase
```

Couchbase local: http://localhost:8091

# Spark Local Setup

- Repo: https://github.com/nhamhung/spark-gcp-project

- Spark: https://mvnrepository.com/search?q=org.apache.spark

- Spark Streaming + Kafka Integration: https://spark.apache.org/docs/latest/streaming-kafka-0-10-integration.html

- Couchbase Spark Connector: https://docs.couchbase.com/spark-connector/current/getting-started.html

- Spark Project: https://medium.com/@suffyan.asad1/spark-essentials-a-guide-to-setting-up-and-running-spark-projects-with-scala-and-sbt-80e2680d3528

- Important settings:

```
# build.sbt:

assembly / assemblyMergeStrategy := {
  case PathList("META-INF", "services", _*) => MergeStrategy.concat
  case PathList("META-INF", xs @ _*) => MergeStrategy.discard
  case x => MergeStrategy.first
}

fork := true

# plugins.sbt:

addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "2.1.5")

# SparkSession

sparkSession.config("spark.driver.bindAddress", "127.0.0.1")

# VM options for both Application and ScalaTest:
--add-exports java.base/sun.nio.ch=ALL-UNNAMED
```

# Spark Jar + GCS Setup

- Create bucket `project-gcp-453004-bucket`

```
sbt clean compile assembly

gcloud storage cp \~/spark/target/scala-2.13/spark-assembly-0.1.0-SNAPSHOT.jar gs://project-gcp-453004-bucket

gcloud storage objects list gs://project-gcp-453004-bucket
```

# DataProc Serverless

```
gcloud dataproc batches list --region=asia-southeast1

gcloud dataproc batches delete spark --region=asia-southeast1

gcloud dataproc batches submit spark --version=2.2 --region=asia-southeast1 --batch=spark --class=com.spark.example.Main --jars=gs://project-gcp-453004-bucket/spark-assembly-0.1.0-SNAPSHOT.jar -- --output-path gs://project-gcp-453004-bucket/transaction-table
```

# BigQuery Setup

- Create a dataset in `asia-southeast1`

```
CREATE OR REPLACE EXTERNAL TABLE
`database.transaction_table` (id INTEGER, name STRING, price INTEGER)
WITH PARTITION COLUMNS (date STRING, hour STRING)
OPTIONS (
  format = "PARQUET",
  uris = ["gs://project-gcp-453004-bucket/transaction-table/*"],
  hive_partition_uri_prefix = "gs://project-gcp-453004-bucket/transaction-table",
  require_hive_partition_filter = TRUE
)

SELECT * FROM `database.transaction_table` WHERE date = '2025-03-08';
```
