#!/usr/bin/python3
"""Shebang"""
from models.base_model import BaseModel


class User(BaseModel):
    """Initialization of class User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
    