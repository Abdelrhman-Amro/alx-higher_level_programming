#!/usr/bin/python3
""" SQLAlchemy """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys

if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost:3360/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(engine)
    session = Session()
    q = session.query(State).order_by(State.id).first()
    if q is None:
        print('Nothing')
    else:
        print("{}: {}".format(q.id, q.name))
    session.close()
