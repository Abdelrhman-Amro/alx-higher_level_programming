#!/usr/bin/python3
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
)

cur = mydb.cursor()
cur.execute("SHOW DATABASES")

print (f"DATABASE save in type -> {type(cur)}")
for db in cur:
    print(db)
