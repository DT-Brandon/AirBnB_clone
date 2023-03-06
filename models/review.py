#!/usr/bin/python3
"""""base_model.py contains the model superclass that will serve for
all classes in the airBnN project
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class of a Review"""
    place_id = ""
    user_id = ""
    text = ""

