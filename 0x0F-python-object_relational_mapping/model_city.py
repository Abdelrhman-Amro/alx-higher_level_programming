#!/usr/bin/python3
""" SQLAlchemy """
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """ City Class """
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
