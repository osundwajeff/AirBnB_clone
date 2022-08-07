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
        self.created_at = datetime.today()

        if len(kwargs) != 0:
            for a, b in kwargs.items():
                if a == "creeated_at" or a == "updated_at":
                    self.__dict__[a] = datetime.strptime(b, time_format)
                else:
                    self.__dict__[k] = b
        else:
            models.storage.new(self)
