#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa
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
    obj = db.query(State).filter_by(id=2).first()
    obj.name = "New Mexico"
    db.commit()
    db.close()
