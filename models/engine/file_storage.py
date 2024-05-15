import json
import os

class FileStorage:
    """
    Class that serializes instances to a JSON file and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
    
    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        json_objects = {}
              # Iterate over all items in __objects
        for key, obj in self.__objects.items():
            # Convert each object to a dictionary using its to_dict method
            obj_dict = obj.to_dict()
            
            # Add the dictionary representation of the object to json_objects
            json_objects[key] = obj_dict

            with open(self.__file_path, 'w') as f:
            #serialize the json_objects dictonry to the json file 
                json.dump(json_objects, f)
    
    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. 
        If the file doesn’t exist, no exception should be raised)

        """
        def reload(self):
            """
            Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists;
            otherwise, do nothing. If the file doesn’t exist
            , no exception should be raised).
            """
            try:
                with open(self.__file_path, 'r') as f:
                    loaded_objects = json.load(f)
                    for key, value in loaded_objects.items():
                        self.__objects[key] = value
            except FileNotFoundError:
                pass  # No action needed if the file doesn't exist


