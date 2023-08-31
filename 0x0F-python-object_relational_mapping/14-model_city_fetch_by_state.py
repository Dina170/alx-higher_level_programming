#!/usr/bin/python3
"""
Prints all City objects from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State).join(State):
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()