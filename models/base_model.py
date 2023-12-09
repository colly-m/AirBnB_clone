#!/usr/bin/python3
"""Module class-model to define all common methods or attributes for other classes"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """Module to define a class BaseModel"""
    def __init__(self, *args, **kwargs):
	"""Initializes base class instance arguments"""
	if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
	    self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
	    storage.new(self)

    def save(self):
	from models import storage
        self.updated_at = datetime.now()
	storage.save()


    def to_dict(self):
        class_name = self.__class__.__name__
        data = self.__dict__.copy()
        data['__class__'] = class_name
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
