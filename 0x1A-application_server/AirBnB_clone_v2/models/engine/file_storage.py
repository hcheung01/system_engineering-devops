#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to JSON file and deserializes back to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary
        """
        if cls is None:
            return self.__objects
        return {k: v for k, v in self.__objects.items() if type(v) == cls}

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        objs_dict = {}
        for key, value in FileStorage.__objects.items():
            objs_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as fd:
            json.dump(objs_dict, fd)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ deletes object in __objects
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects.pop(key)
            self.save()
        else:
            return

    def close(self):
        """deserialize the JSON file to objects"""
        self.reload()
