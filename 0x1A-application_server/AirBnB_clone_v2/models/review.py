#!/usr/bin/python3
"""This is the review class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class Review(BaseModel, Base):
    """This is the class for Review
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60),
                          ForeignKey("places.id", ondelete='cascade'),
                          nullable=False)
        user_id = Column(String(60),
                         ForeignKey("users.id", ondelete='cascade'),
                         nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
