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
    # (1, 'San Francisco', 'California')
    # Results must be sorted in ascending order by cities.id
    query = """
            SELECT c.id, c.name, s.name
            FROM cities AS c
            INNER JOIN states AS s
            ON c.state_id = s.id
            ORDER BY c.id
            """
    cur.execute(query)

    # fetch
    rows = cur.fetchall()
    for r in rows:
        print(r)

    cur.close()
    db.close()
