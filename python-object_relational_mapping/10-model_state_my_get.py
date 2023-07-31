#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
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

    obj = db.query(State).filter_by(name=argv[4]).first()

    if obj:
        print(obj.id)
    else:
        print("Not found")

   session.close() 
