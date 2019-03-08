#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """

    __tablename__ = 'cities'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60),
                          ForeignKey("states.id"),
                          nullable=False)
        places = relationship("Place", cascade='all')
    else:
        state_id = ""
        name = ""
