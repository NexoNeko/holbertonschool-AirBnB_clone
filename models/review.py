#!/usr/bin/python3
"""Shebang"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Initialization of the class Review"""

    place_id = ""
    user_id = ""
    text = ""
