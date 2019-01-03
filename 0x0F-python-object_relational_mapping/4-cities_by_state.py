#!/usr/bin/python3
'''lists all cities from database'''

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # connect
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    # cursor
    c = db.cursor()

    # execute
    cmd = "SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON cities.state_id = states.id"
    c.execute(cmd)

    # fetch
    rows = c.fetchall()

    # print
    for row in rows:
        print(row)

    # close
    c.close()
    db.close()
