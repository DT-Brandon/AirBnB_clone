#!/usr/bin/python3
"""""base_model.py contains the model superclass that will serve for
all classes in the airBnN project
"""
from models.base_model import BaseModel


class User(BaseModel):
    """class of a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

