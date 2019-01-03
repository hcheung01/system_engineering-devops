#!/usr/bin/python3
'''Define get function'''
import MySQLdb


def main():
    # 3 arguments take in
    # make a connection
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         database=argv[3])

    # create a cursor
    c = db.cursor()

    # execute query
    c.execute('SELECT * FROM states ORDER BY id ASC')
    rows = c.fetchall()
    for i in rows:
        print(i)

    # close all cursor and database
    c.close()
    db.close()

if __name__ == "__main__":
    from sys import argv
    main()
