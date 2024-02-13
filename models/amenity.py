#!/usr/bin/python3
"""The `amenity` module.

This module defines the `Amenity` class, which is a 
subclass of the `BaseModel` class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity provided by a place or house.

    Attributes:
        name: The name of the amenity.
    """

    name = ""
