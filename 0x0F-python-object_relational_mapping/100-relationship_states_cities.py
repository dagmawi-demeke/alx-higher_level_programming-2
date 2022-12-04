#!/usr/bin/python3
"""Start link class to table in database 
"""


import sys
from relationship_city import Base, City
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    s = State(name = "California")
    c = City(name = "San Francisco")
    session.add(s)
    session.add(c)
    session.commit()