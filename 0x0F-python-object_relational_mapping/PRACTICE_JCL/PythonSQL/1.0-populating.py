#!/usr/bin/python3
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="py_sql"
)

cur = mydb.cursor()

sqlFormula = "INSERT INTO students(name, age) VALUES(%s, %s)"
student_1 = ("Abdelrhman", 21)
cur.execute(sqlFormula, student_1)

# Puplish changes to databse
mydb.commit()
