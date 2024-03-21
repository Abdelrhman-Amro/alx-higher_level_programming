#!/usr/bin/python3
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="py_sql"
)

cur = mydb.cursor()

sqlFormula = "SELECT * FROM students"
cur.execute(sqlFormula)

# Fetch all of the rows from the last executed statement
res = cur.fetchall()
for row in res:
    print(row)

cur.execute(sqlFormula)
# Fetch first row only
res = cur.fetchone()
print(f"first row is -----> {res}")
