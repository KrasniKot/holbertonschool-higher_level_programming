#!/usr/bin/python3
"""
Takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    with MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306, charset="utf8") as db:
        db = db.cursor()
        db.execute(
            "SELECT cities.name FROM cities INNER JOIN states\
                    ON cities.state_id = states.id WHERE states.name LIKE\
                    %s ORDER BY cities.id ASC",
            (argv[4],))
        datable = db.fetchall()
        for idx, row in enumerate(datable):
            if idx != 0:
                print(", ", end="")
            print(row[0], end="")
        print()
