#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

db = MySQLdb.connect(
    host='localhost',
    user=sys.argv[1],
    password=sys.argv[2],
    database=sys.argv[3],
    port=3306
)

cur = db.cursor()

query = "select * from states"
cur.execute(query)

rows = cur.fetchall()
for row in rows:
    print(row)
    
cur.close()
db.close()
