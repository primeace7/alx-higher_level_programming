#!/usr/bin/python3
'''
a script that takes in an argument and displays all values in the states
  table of hbtn_0e_0_usa where name matches the argument
Results must be sorted in ascending order by states.id
'''

import MySQLdb as DB
import sys

if __name__ == '__main__':
    config = {'user': sys.argv[1], 'passwd': sys.argv[2], 'db': sys.argv[3],
              'host': "localhost", 'port': 3306}
    db_connect = DB.connect(**config)
    cursor = db_connect.cursor()

    state = sys.argv[-1]
    query = '''SELECT cities.name
    FROM cities
    WHERE state_id =
    (SELECT states.id
    FROM states
    WHERE states.name = %s
    LIMIT 1)
    ORDER BY cities.id ASC;'''

    cursor.execute(query, (state,))

    rows = cursor.fetchall()

    for row in rows:
        if row == rows[-1]:
            ending = '\n'
        else:
            ending = ', '
        print(row[0], end=ending)

    cursor.close()
    db_connect.close()
