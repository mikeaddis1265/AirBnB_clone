import json
import os
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)