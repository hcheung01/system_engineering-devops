#!/usr/bin/python3
"""This is the DBStorage class for AirBnB"""
import json
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, scoped_session
import os


class DBStorage():
    """ Database storage class """

    __engine = None
    __session = None

    def __init__(self):
        """ initialization """

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB'),
            pool_pre_ping=True))

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ get dictionary of all objects """

        if cls is None:
            all_list = []
            for x in BaseModel.__subclasses__():
                all_list.extend(self.__session.query(x).all())
            return {"{}.{}".format(type(obj).__name__, obj.id): obj
                    for obj in all_list}

        if type(cls) is str:
            cls = eval(cls)

        return {"{}.{}".format(type(obj).__name__, obj.id): obj
                for obj in self.__session.query(cls).all()}

    def new(self, obj):
        """ insert new object in current database session """
        self.__session.add(obj)

    def save(self):
        """ commit changes to database """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from current database session """

        if obj is not None:
            all_instances = self.__session.query(obj.__class__.__name__).all()
            for instance in all_instances:
                if obj == instance:
                    self.__session.delete(obj)
                    self.save()

    def reload(self):
        """ reload database """

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """close session"""
        self.__session.close()
