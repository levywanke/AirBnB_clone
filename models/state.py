#!/usr/bin/python3
"""The `state` module.

This module defines the `State` class,
which is a subclass of the `BaseModel` class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state within the application.

    Attributes:
        name: The name of the state.
    """
    name = ""
