#!/usr/bin/python3
"""""base_model.py contains the model superclass that will serve for
all classes in the airBnN project
"""
import datetime
import json
import os


class FileStorage:
    """class used to store user data in json format"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all objects in file"""
        return FileStorage.__objects

    def new(self, obj):
        """used to store a new object in __object dict"""
        obj_key = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """ Serializes __objects to JSON file."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fileName:
            object_dict = {k: v.to_dict()
                           for k, v in FileStorage.__objects.items()}
            json.dump(object_dict, fileName)

    def reload(self):
        """Deserializes JSON file into __objects."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as fileName:
            obj_dict = json.load(fileName)
            obj_dict = {k: self.classes()[v['__class__']](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def attributes(self):
        """Returns the valid attributes of all classes"""
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
