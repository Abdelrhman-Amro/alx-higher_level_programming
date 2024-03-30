#!/usr/bin/python3
""" MySQLdb """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306
    )
    cur = db.cursor()

    query = ""
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
