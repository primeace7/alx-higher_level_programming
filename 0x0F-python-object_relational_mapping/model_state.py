#!/usr/bin/python3
'''
implement a class that contains a SQLAlchemy definition of State and
an instance Base = declarative_base():
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name
#        self.id = id
