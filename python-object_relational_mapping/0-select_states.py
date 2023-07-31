#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa:
"""


if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    with MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8") as db:
        db = db.cursor()
        db.execute("SELECT * FROM states ORDER BY states.id ASC")
        datable = db.fetchall()

        for row in datable:
            print(row)
