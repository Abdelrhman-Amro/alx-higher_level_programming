#!/usr/bin/python3
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="py_sql"
)

cur = mydb.cursor()

sqlFormula = "INSERT INTO students(name, age) VALUES(%s, %s)"
students = [("Ahmed", 13),
            ("Noor", 18),
            ("Omar", 10),
            ("Nesma", 5),
            ("Youssef", 25),
            ("Mohamed", 9)]

# Notice here we use (executemany) instead of (execute)
cur.executemany(sqlFormula, students)

# Puplish changes to databse
mydb.commit()
