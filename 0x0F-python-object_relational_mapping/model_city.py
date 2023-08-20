#!/usr/bin/python3
"""
Defines a City class that inherits from SQLAlchemy Base class.
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class

    Attributes:
        __tablename__ (str): The table name
        id (int): The City id
        name (str): The City name
        state_id (int): The City's state id

    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
