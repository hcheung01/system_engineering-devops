#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = "states"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """getter"""
            all_cities = models.storage.all(models.City)
            return [c for c in all_cities.values() if c.state_id == self.id]
