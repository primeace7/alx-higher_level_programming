#!/usr/bin/python3

import MySQLdb as DB
db_connect = DB.connect(host='localhost', port=3306, user='root',\
                        passwd='root', db='hbtn_0e_0_usa')
cursor = db_connect.cursor()
cursor.execute('SELECT * FROM hbtn_0e_0_usa.states ORDER BY id ASC')

rows = cursor.fetchall()

for row in rows:
    print(row)
cursor.close()
db_connect.close()
