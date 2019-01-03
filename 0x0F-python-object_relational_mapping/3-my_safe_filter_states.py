#!/usr/bin/python3
"""Filter states by user input"""
import MySQLdb

def main():

    if len(argv) == 5:
        # connect
        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=argv[1],
                             passwd=argv[2],
                             db=argv[3]
        )
        # cursor
        c = db.cursor()

        # execute query
        c.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC", (argv[4], ))

        # fetch
        rows = c.fetchall()

        # print
        for row in rows:
            print(row)

        # close
        c.close()
        db.close()
    else:
        return

if __name__ == "__main__":
    from sys import argv
    main()
