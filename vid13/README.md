# sqlite3 commands

```
# Connect to DB

sqlite3 DB_NAME

# List tables

.tables

# Show table schema

.schema TABLE_NAME

# Change mode

.mode column
```

# Phan II Cau 2

```
# Cau 2.c

SELECT *
FROM TINH JOIN DANSO
  ON TINH.maTinh = DANSO.maTinh;

# Cau 2.d

SELECT TINH.tenTinh, DANSO.nam, DANSO.danSoTB
FROM TINH JOIN DANSO
  ON TINH.maTinh = DANSO.maTinh
WHERE DANSO.nam = 2020;
```

# Phan II Cau 6

```
# Cau 6.a

SELECT *
FROM KHUVUC INNER JOIN (DIAPHUONG INNER JOIN DAUTU ON DIAPHUONG.maDP = DAUTU.maDP)
  ON KHUVUC.maKV = DIAPHUONG.maKV;

# Cau 6.d

SELECT KHUVUC.tenKV, DIAPHUONG.tenDP, DAUTU.nam, DAUTU.tongVon
FROM KHUVUC INNER JOIN (DIAPHUONG INNER JOIN DAUTU ON DIAPHUONG.maDP = DAUTU.maDP)
  ON KHUVUC.maKV = DIAPHUONG.maKV;
```
