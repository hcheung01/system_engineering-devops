#!/usr/bin/python3
'''Script to list all states with a name starting with N'''
import MySQLdb

def main():
    # connect
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # cursor
    c = db.cursor()

    # execute query
    c.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY id ASC')

    # fetch and print
    rows = c.fetchall()
    for row in rows:
        print(row)

    # close cursor and database
    c.close()
    db.close()

if __name__ == "__main__":
    from sys import argv
    main()
