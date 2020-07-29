#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
import os


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float2
        amenity_ids: list of Amenity ids
    """

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60),
                         ForeignKey('cities.id', ondelete='cascade'),
                         nullable=False)
        user_id = Column(String(60),
                         ForeignKey('users.id', ondelete='cascade'),
                         nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review',
                               cascade='delete', backref='place')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False)
    else:
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """getter attribute"""
            return [review for review in models.storage.all(Review).values()
                    if self.id == review.place_id]

        @property
        def amenities(self):
            """getter attribute
            """
            return [amenity for amenity in models.storage.all(Amenity).values()
                    if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """setter method"""
            if obj and isinstance(obj, Amenity):
                type(self).amenity_ids.append(obj.id)
