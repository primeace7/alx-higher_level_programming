#!/usr/bin/python3
'''
implement a class that contains a SQLAlchemy definition of State and
an instance Base = declarative_base():
'''


from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import Base, State
import sys


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".\
                       format(sys.argv[1], sys.argv[2], sys.argv[3]))

    with Session(engine) as session:
        del_states = session.query(State).filter\
            (State.name.ilike('%a%')).delete()
        session.commit()
