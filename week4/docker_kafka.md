# Use Docker to create a simple Kafka cluster

- Use Bitnami Kafka image
- Download baseline Docker Compose file
  `curl -sSL https://raw.githubusercontent.com/bitnami/containers/main/bitnami/kafka/docker-compose.yml > docker-compose.yml`
- Modify to allow for both internal and external clients

# Run docker-compose

- `docker-compose up -d` for running in detached mode
- `docker ps` to list running containers
- `docker exec -it kafka bash` to access Bash shell of running container

# Test out Producer and Consumer for internal client

- Open 2 terminals, one for consumer and one for producer
- Producer:
  `kafka-console-producer.sh --bootstrap-server kafka:9092 --topic test`
- Consumer:
  `kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic test`

# Write an application for Producer and Consumer for external client

- Mvn dependency: https://mvnrepository.com/artifact/org.apache.kafka/kafka-clients/3.5.1
- Kafka API: https://kafka.apache.org/documentation
