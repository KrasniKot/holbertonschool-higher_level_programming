#!/usr/bin/python3
"""
File that contains the class definition of a State
and an instance Base = declarative_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float


Base = declarative_base()


class State(Base):
    """ Defines a state model """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(129), nullable=False)
