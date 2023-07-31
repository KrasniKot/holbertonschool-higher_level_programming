#!/usr/bin/python3
"""
Deletes all State objects with a name
containing the letter 'a' from the database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    db = Session()

    states = db.query(State).filter(
            State.name.like('%a%')).all()

    for state in states:
        db.delete(state)
    db.commit()

    db.close()
