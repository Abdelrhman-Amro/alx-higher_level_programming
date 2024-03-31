#!/usr/bin/python3
""" SQLAlchemy """
from sqlalchemy.orm import session, sessionmaker
from sqlalchemy import create_engine
from model_city import City
from model_state import State
import sys


if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost:3360/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(engine)
    session = Session()

    q = session.query(State, City).join(City, State.id == City.id)\
        .order_by(City.id)
    for row in q:
        # <state name>: (<city id>) <city name>
        print("{}: ({}) {}".format(row.State.name, row.City.id, row.City.name))

    session.close()
