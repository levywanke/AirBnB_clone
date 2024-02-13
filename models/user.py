#!usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """GENERATION OF a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
