#!/usr/bin/python3
'''
a script that lists all states with a name starting with N (upper N)
  om the database hbtn_0e_0_usa
Results must be sorted in ascending order by states.id
'''
import MySQLdb as DB
import sys

if __name__ == '__main__':
    config = {'user': sys.argv[1], 'passwd': sys.argv[2], 'db': sys.argv[3],
              'host': "localhost", 'port': 3306}

    db_connect = DB.connect(**config)
    cursor = db_connect.cursor()

    query = """SELECT * FROM states WHERE states.name\
     LIKE "N%" ORDER BY states.id ASC;"""
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db_connect.close()
