#!/usr/bin/python3
"""Shebang"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City


class FileStorage:
    """Initialization of the class FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Function that returns the dictionary (objects)
        from FileStorage class"""
        return self.__objects

    def new(self, obj):
        """Sets a new object in __objects,
        with the class name as the key"""
        if obj is not None:
            newKey = obj.__class__.__name__ + "." + obj.id
            FileStorage.__objects[newKey] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as f:
            objects_json = {}
            for key, value in self.__objects.items():
                objects_json[key] = value.to_dict()
            json.dump(objects_json, f)

    def reload(self):
        """Desearilzes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                objects_json = json.load(f)
                for key, value in objects_json.items():
                    obj_class = value['__class__']
                    obj = eval(obj_class + "(**value)")
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
