#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import String, Integer, Column
from models import place
import os


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place.place_amenity,
                                       viewonly=False)
    else:
        name = ''
