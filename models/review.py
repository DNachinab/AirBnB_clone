#!/usr/bin/python3
"""Module creates Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class for controlling review objects"""

    place_id = ""
    user_id = ""
    text = ""
