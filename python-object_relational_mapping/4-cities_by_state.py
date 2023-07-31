#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    with MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306, charset="utf8") as db:
        db = db.cursor()
        db.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities INNER JOIN states\
                    ON cities.state_id=states.id ORDER by cities.id ASC")
        table = db.fetchall()
        for data in table:
            print(data)
