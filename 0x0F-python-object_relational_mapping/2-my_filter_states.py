#!/usr/bin/python3
'''
a script that takes in an argument and displays all values in the states
  table of hbtn_0e_0_usa where name matches the argument
Results must be sorted in ascending order by states.id
'''

import MySQLdb as DB
import sys

if __name__ == '__main__':
    db_connect = DB.connect(user='root', passwd='root', db='hbtn_0e_0_usa')
    cursor = db_connect.cursor()
    cursor.execute("""SELECT * FROM states WHERE name=%s ORDER\
    BY states.id ASC""", (sys.argv[-1],))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db_connect.close()
