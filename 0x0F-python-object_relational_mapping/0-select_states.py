#!/usr/bin/python3
'''
a script that lists all states from the database hbtn_0e_0_usa
Results must be sorted in ascending order by states.id
'''

if __name__ == '__main__':
    import MySQLdb as DB
    db_connect = DB.connect(host='localhost', port=3306, user='root',
                            passwd='root', db='hbtn_0e_0_usa', charset='utf8')
    cursor = db_connect.cursor()
    cursor.execute("""SELECT * FROM states ORDER BY `id` ASC""")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db_connect.close()
