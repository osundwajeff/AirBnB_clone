#!/usr/bin/python3
""" Base model class """
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Basemodel HBnB project"""

    def __init__(self, *args, **kwargs):
        """ initialize new BaseModel.
        Args:
            *args (any): any arguments.
            **kwargs (dict): key/value pair attributes
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for a, b in kwargs.items():
                if a == "created_at" or a == "updated_at":
                    self.__dict__[a] = datetime.strptime(b, time_format)
                else:
                    self.__dict__[a] = b
        else:
            models.storage.new(self)

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance """
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__>
        of the BaseModel instance """
        class_name = self.__class__.__name__

        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
