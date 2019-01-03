#!/usr/bin/python3
'''script to list all cities with user inputted state'''

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    # connect
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3]
                         )
    # cursor
    c = db.cursor()
    # execute
    state = (argv[4], )
    cmd = "SELECT cities.name FROM cities JOIN states ON\
    cities.state_id = states.id AND states.name = %s ORDER BY cities.id ASC"

    c.execute(cmd, state)

    # fetch
    rows = c.fetchall()

    # print
    ll = [x[0] for x in rows]
    together = ", ".join(ll)
    print(together)

    # close
    c.close()
    db.close()
