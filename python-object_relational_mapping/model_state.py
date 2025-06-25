#!/usr/bin/python3
"""
..
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    Define class states.
    """
    __tablename__ = 'states'

    id = Column(Integer, auto_increment=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
