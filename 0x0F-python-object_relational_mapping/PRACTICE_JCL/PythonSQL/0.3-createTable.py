#!/usr/bin/python3
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="py_sql"
)

cur = mydb.cursor()
cur.execute("CREATE TABLE students(name VARCHAR(255), age INTEGER)")
