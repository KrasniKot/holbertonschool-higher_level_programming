#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    db = Session()
    db.add(State(name="Louisiana"))
    db.commit()

    for data in db.query(State).filter_by(name="Louisiana"):
        print(data.id)
    db.close()
