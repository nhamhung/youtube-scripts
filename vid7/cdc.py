from kafka import KafkaConsumer
import json
from sqlalchemy import create_engine, text

# MySQL & PostgreSQL Database Configurations
MYSQL_DB_URL = "mysql+pymysql://mysqluser:mysqlpw@localhost:3306/inventory"
POSTGRES_DB_URL = "postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/postgres"

# Connect to PostgreSQL
pg_engine = create_engine(POSTGRES_DB_URL)

# Kafka Consumer to Read CDC Events from Debezium
consumer = KafkaConsumer(
    'dbserver1.inventory.customers',  # Change topic as needed
    bootstrap_servers='localhost:9092',
    # value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

def apply_cdc_event(event):
    """Apply MySQL CDC event to PostgreSQL."""
    payload = event['payload']
    op = payload['op']  # "c" (create), "u" (update), "d" (delete)
    before = payload.get('before')  # Before change
    after = payload.get('after')  # After change

    print(f"op, before, after = {op}, {before}, {after}")

    with pg_engine.connect() as conn:
        if op == "c":  # Insert
            query = text("""
                INSERT INTO customers (id, first_name, last_name, email) 
                VALUES (:id, :first_name, :last_name, :email)
                ON CONFLICT (id) DO NOTHING;
            """)
            conn.execute(query, after)

        elif op == "u":  # Update
            query = text("""
                UPDATE customers 
                SET first_name=:first_name, last_name=:last_name, email=:email 
                WHERE id=:id;
            """)
            conn.execute(query, after)

        elif op == "d":  # Delete
            query = text("DELETE FROM customers WHERE id=:id;")
            conn.execute(query, {"id": before["id"]})

        conn.commit()

# Listen for CDC Events
print("Listening for changes...")
for message in consumer:
    if message.value: # Message can have None value due to Debezium's Tombstone event for Kafka log compaction
      apply_cdc_event(json.loads(message.value.decode('utf-8')))