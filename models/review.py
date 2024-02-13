#!/usr/bin/python3
"""The `review` module.

This module defines the `Review` class, which is
 a subclass of the `BaseModel` class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review of a place or house.

    This class encapsulates a review posted by users
    of the application regarding a place or house.

    Attributes:
        text: The content of the review.
        user_id: The ID of the user who posted the review.
        place_id: The ID of the place/house being reviewed.
    """
    text = ""
    user_id = ""
    place_id = ""
