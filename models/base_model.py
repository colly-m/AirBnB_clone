#!/usr/bin/python3
"""BaseModel that defines all attributes/methods for classes of Airbnb"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defining a class base model"""

    def __init__(self, *args, **kwargs):
        """Initialization of base class instance
        Args:
            *args: arguments
            **kwargs: key-value arguments
        """
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

    def __str__(self):
        """Defining str method"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Defining save method"""
        from models import storage  # Import with the methond
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Defining to_dict method"""
        data = self.__dict__.copy()
        data['__class__'] = type(self).__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
