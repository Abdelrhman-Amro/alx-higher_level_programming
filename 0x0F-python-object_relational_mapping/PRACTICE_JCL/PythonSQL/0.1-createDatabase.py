#!/usr/bin/python3
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
)

cur = mydb.cursor()
cur.execute("CREATE DATAPASE py_sql")
