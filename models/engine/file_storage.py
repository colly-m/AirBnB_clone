#!/usr/bin/python3
"""Module to define a class FileStorage"""
import json
import models
import os
import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review


class FileStorage:
    """Defines a class FileStorage"""
    __file__path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objests in dictionary also accessing all stored objects"""
        return (self.__objects)

    def new(self, obj):
        """Adds an object into a dictionary with <obj class name>.id key"""
        obj_cls_name = obj.__class__.__name__

        key = "{}.{}".format(obj_cls_name, obj.id)

        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects dictionary to JSON format and saves to specified
        __file_path
        """
        data = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as fd:
            json.dump(data, fd)

    def objs_classes(self):
	"""Returns classes dictionay"""
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
        """
        Reload the file and deserializes JSON into __objects
        """

        try:
            with open(FileStorage.__file_path, encoding="utf-8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, obj in FileStorage.__objects.items():
                class_name = obj["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**value)
        except FileNotFoundError:
            pass

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
