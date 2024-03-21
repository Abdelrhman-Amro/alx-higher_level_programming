#!/usr/bin/python3
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="py_sql"
)

cur = mydb.cursor()
cur.execute("SHOW TABLES")

for tb in cur:
    print(tb)
