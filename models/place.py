#!/usr/bin/python3
"""""base_model.py contains the model superclass that will serve for
all classes in the airBnN project
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """class of a Place"""
    city_id = ""
    name = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
