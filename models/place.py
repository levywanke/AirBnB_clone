#!/usr/bin/python3
"""The `place` module.

This module defines the `Place` class,
which is a subclass of the `BaseModel` class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place or house within the application.

    This class encapsulates a place or house uploaded
    by users of the application.

    Attributes:
        name: The name of the place/house.
        user_id: The ID of the user who uploaded the place/house.
        city_id: The ID of the city where the place/house is located.
        description: A description of the place/house.
        number_bathrooms: The number of bathrooms in the place/house.
        price_by_night: The price per night to stay at the place/house.
        number_rooms: The number of rooms in the place/house.
        longitude: The longitude coordinate of the place/house location.
        latitude: The latitude coordinate of the place/house location.
        max_guest: The maximum number of guests allowed at the place/house.
        amenity_ids: A list of IDs representing
        amenities available at the place/house.
    """

    name = ""
    user_id = ""
    city_id = ""
    description = ""
    number_bathrooms = 0
    price_by_night = 0
    number_rooms = 0
    longitude = 0.0
    latitude = 0.0
    max_guest = 0
    amenity_ids = []
