#!/usr/bin/python3
"""Module class-model to define all common methods or attributes for other classes"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """Module to define a class BaseModel"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

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
