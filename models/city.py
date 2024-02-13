#!/usr/bin/python3
"""The `city` module.

This module defines the `City` class,
which is a subclass of the `BaseModel` class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city within the application.

    Attributes:
        name: The name of the city.
        state_id: The ID of the state to which the city belongs.
    """
    name = ""
    state_id = ""
