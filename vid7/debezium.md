# Overview

1. Set up GCP VM instance (Debian)
2. Set up Kafka + ZooKeeper
3. Set up MySQL database with mock data
4. Set up MySQL client
5. Set up

# Set up GCP VM instance

- SSH

```
gcloud compute ssh --project=project-gcp-453004 --zone=asia-southeast1-b instance-20250315-181610
```

- Install Docker

https://docs.docker.com/engine/install/debian/

```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo docker ps
```

# Setup Kafka + Zookeeper

```
sudo docker run -d --name zookeeper -p 2181:2181 -p 2888:2888 -p 3888:3888 quay.io/debezium/zookeeper:3.0

sudo docker run -d --name kafka --link zookeeper:zookeeper -p 9092:9092 quay.io/debezium/kafka:3.0

sudo docker logs zookeeper
sudo docker logs kafka
```

# Setup Mysql + Postgresql

- Mysql

```
sudo docker run -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=debezium -e MYSQL_USER=mysqluser -e MYSQL_PASSWORD=mysqlpw quay.io/debezium/example-mysql:3.0

sudo docker run -it --rm --name mysqlterm --link mysql mysql:8.2 sh -c 'exec mysql -h"mysql" -P"3306" -umysqluser -p"mysqlpw"'

show databases;
use inventory;
show tables;
show create table customers;
```

- Postgresql

```
sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres

sudo docker run -it --rm --link postgres --name postgresqlterm postgres sh -c 'exec psql -h postgres -p 5432 -U postgres -d postgres'

CREATE TABLE customers (
id SERIAL PRIMARY KEY,
first_name VARCHAR(255) NOT NULL,
last_name VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL UNIQUE
);

\dt

INSERT INTO customers (id, first_name, last_name, email) VALUES
(1001, 'Sally', 'Thomas', 'sally.thomas@acme.com'),
(1002, 'George', 'Bailey', 'gbailey@foobar.com'),
(1003, 'Edward', 'Walker', 'ed@walker.com'),
(1004, 'Anne', 'Kretchmar', 'annek@noanswer.org');
```

# Setup Mysql Debezium Connector and Kafka client

- Connector

https://debezium.io/documentation/reference/stable/tutorial.html#starting-zookeeper

```
sudo docker run -d --name connect -p 8083:8083 -e GROUP_ID=1 -e CONFIG_STORAGE_TOPIC=my_connect_configs -e OFFSET_STORAGE_TOPIC=my_connect_offsets -e STATUS_STORAGE_TOPIC=my_connect_statuses --link kafka:kafka --link mysql:mysql quay.io/debezium/connect:3.0

curl -H "Accept:application/json" localhost:8083/

curl -H "Accept:application/json" localhost:8083/connectors/

curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ -d '{ "name": "inventory-connector", "config": { "connector.class": "io.debezium.connector.mysql.MySqlConnector", "tasks.max": "1", "database.hostname": "mysql", "database.port": "3306", "database.user": "debezium", "database.password": "dbz", "database.server.id": "184054", "topic.prefix": "dbserver1", "database.include.list": "inventory", "schema.history.internal.kafka.bootstrap.servers": "kafka:9092", "schema.history.internal.kafka.topic": "schemahistory.inventory" } }'

curl -H "Accept:application/json" localhost:8083/connectors/

curl -i -X GET -H "Accept:application/json" localhost:8083/connectors/inventory-connector
```

- Kafka client

```
sudo apt update
sudo apt install default-jre
sudo apt install jq -y

curl -O https://dlcdn.apache.org/kafka/3.9.0/kafka_2.13-3.9.0.tgz
tar -xzf kafka_2.13-3.9.0.tgz

kafka_2.13-3.9.0/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic dbserver1.inventory.customers --from-beginning | jq
```

# Setup Conda and Python application

https://www.anaconda.com/docs/getting-started/miniconda/install#quickstart-install-instructions

```
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh

source ~/miniconda3/bin/activate

conda init --all
```

```
conda create -n cdc_env python=3.10 conda-forge::kafka-python conda-forge::sqlalchemy conda-forge:psycopg2 conda-forge:pymysql -y

conda activate cdc_env

vim cdc.py
```

# Verify CDC in action

- Mysql

```
UPDATE customers SET first_name='Anne Marie' WHERE id=1004;

DELETE FROM addresses WHERE customer_id=1003;
DELETE FROM orders WHERE purchaser=1003;
DELETE FROM customers WHERE id=1003;

INSERT INTO customers (id, first_name, last_name, email) VALUES
(1005, 'Tom', 'Sawyer', 'tom.sawyer@barfoo.com');
```
