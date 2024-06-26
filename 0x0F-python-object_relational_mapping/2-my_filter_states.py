#!/usr/bin/python3
""" MySQLdb """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3])
    cur = db.cursor()

    query = """SELECT * FROM states
                WHERE BINARY name LIKE '{}'
                ORDER BY states.id""".format(sys.argv[4])
    cur.execute(query)

    # fetch
    rows = cur.fetchall()
    for r in rows:
        print(r)

    cur.close()
    db.close()
