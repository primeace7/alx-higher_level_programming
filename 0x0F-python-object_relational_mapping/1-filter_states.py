#!/usr/bin/python3
'''
a script that lists all states with a name starting with N (upper N)
  om the database hbtn_0e_0_usa
Results must be sorted in ascending order by states.id
'''

if __name__ == '__main__':
    import MySQLdb as DB
    db_connect = DB.connect(user='root', passwd='root', db='hbtn_0e_0_usa')
    cursor = db_connect.cursor()
    cursor.execute("""SELECT * FROM states WHERE name\
    LIKE 'N%' ORDER BY states.id ASC""")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db_connect.close()
