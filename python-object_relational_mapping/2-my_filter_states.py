#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    with MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306, charset="utf8") as db:
        db = db.cursor()
        db.execute("SELECT * FROM states WHERE name LIKE '{}'\
                ORDER BY states.id ASC".format(argv[4])
        datable = db.fetchall()
        for row in datable:
            print(row)
