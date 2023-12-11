#!/usr/bin/python3
"""Module for file storage class"""

import os
import json
import models
import datetime


class FileStorage:
    """Class for a File-storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """Sets new objects"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialazes all files"""
        objs = {}
        for key, val in self.__objects.items():
            objs[key] = val.to_dict()
        with open(self.__file_path, 'w') as fd:
            json.dump(objs, fd)

    def objs_classes(self):
        """Returns dictionary of classes"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place
        from models.city import City
        from models.review import Review

        objs_classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
                }
        return objs_classes

    def reload(self):
        """Deserializes the JSON file to _objects"""
        if not os.path.isfile(self.__file_path):
            return

        with open(self.__file_path, 'r') as fd:
            obj_dict = json.load(fd)
            obj_dict = {key: self.objs_classes()[val["__class__"]](**val)
                        for key, val in obj_dict.items()}
            self.__objects = obj_dict

    def attributes(self):
        """Returns the valid attributes and their types for classname."""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
