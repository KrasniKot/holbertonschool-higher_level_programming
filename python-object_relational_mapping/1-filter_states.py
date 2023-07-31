#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    with MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306) as db:
        db = db.cursor()
        db.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
        datable = db.fetchall()

        for row in datable:
            print(row)

