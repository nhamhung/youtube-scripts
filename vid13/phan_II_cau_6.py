import sqlite3
import os

DB_FILE = "dautu.db"

print("--- Connecting to Database ---")

try:
  conn = sqlite3.connect(DB_FILE)
  cursor = conn.cursor()
  print(f"Successfully connected to {DB_FILE}")
except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")
    exit()

print("\n--- Creating Tables ---")

def execute_query(conn, cursor, query, query_name, table_name):
  try:
    cursor.execute(query)
    conn.commit()
    print(f"Executed {query_name}: {table_name}")
  except sqlite3.Error as e:
    print(f"Error when creating table: {table_name}, {e}")
    exit()

execute_query(conn, cursor, "DROP TABLE IF EXISTS KHUVUC;", query_name="drop table", table_name="KHUVUC")
execute_query(conn, cursor, "DROP TABLE IF EXISTS DIAPHUONG;", query_name="drop table", table_name="DIAPHUONG")
execute_query(conn, cursor, "DROP TABLE IF EXISTS DAUTU;", query_name="drop table", table_name="DAUTU")

khuvuc_create = """
CREATE TABLE IF NOT EXISTS KHUVUC (
    maKV INTEGER PRIMARY KEY,
    tenKV TEXT NOT NULL
);
"""
tinh_create = """
CREATE TABLE IF NOT EXISTS DIAPHUONG (
    maDP INTEGER PRIMARY KEY,
    maKV INTEGER NOT NULL,
    tenDP TEXT NOT NULL,
    FOREIGN KEY(maKV) REFERENCES KHUVUC(maKV)
);
"""
danso_create = """
CREATE TABLE IF NOT EXISTS DAUTU (
    maDP INTEGER NOT NULL,
    nam INTEGER NOT NULL,
    tongVon INTEGER NOT NULL,
    PRIMARY KEY(maDP, nam)
    FOREIGN KEY(maDP) REFERENCES DIAPHUONG(maDP)
);
"""

execute_query(conn, cursor, khuvuc_create, query_name="create table", table_name="KHUVUC")
execute_query(conn, cursor, tinh_create, query_name="create table", table_name="DIAPHUONG")
execute_query(conn, cursor, danso_create, query_name="create table", table_name="DAUTU")

print("\n--- Inserting Data into Tables ---")

khuvuc_insert = """
INSERT INTO KHUVUC (maKV, tenKV) VALUES 
  (1, 'Bac Bo'),
  (2, 'Trung Bo'),
  (3, 'Nam Bo')
"""

tinh_insert = """
INSERT INTO DIAPHUONG (maDP, maKV, tenDP) VALUES 
  (4, 1, 'Thai Nguyen'),
  (5, 2, 'Nghe An'),
  (6, 3, 'Tra Vinh')
"""

danso_insert = """
INSERT INTO DAUTU (maDP, nam, tongVon) VALUES 
  (4, 2020, 123),
  (5, 2021, 213),
  (6, 2020, 312)
"""

execute_query(conn, cursor, khuvuc_insert, query_name="insert table", table_name="KHUVUC")
execute_query(conn, cursor, tinh_insert, query_name="insert table", table_name="DIAPHUONG")
execute_query(conn, cursor, danso_insert, query_name="insert table", table_name="DAUTU")