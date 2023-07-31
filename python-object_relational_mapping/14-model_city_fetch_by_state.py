#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    db = Session()

    for obj in db.query(State.name, City.id, City.name).filter(
            City.state_id == State.id).order_by(City.id):
        print("{}: ({}) {}".format(obj[0], obj[1], obj[2]))

    db.close()
