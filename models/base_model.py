#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            if "created_at" in kwargs:
                kwargs["created_at"] = datetime.fromisoformat(kwargs["created_at"])
            if "updated_at" in kwargs:
                kwargs["updated_at"] = datetime.fromisoformat(kwargs["updated_at"])
            for key, value in kwargs.items():
                if key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()           
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"   

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict
