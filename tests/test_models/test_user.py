#!/usr/bin/python3
""" Tests for specific modules
Modules tested:
- User
- City
- Amenity
- Place
- Review
- State """
import unittest
from models.user import User


class Tests(unittest.TestCase):
    """ Test functions for modules"""

    def test_user_first_name(self):
        """ Testing User attributes"""
        var = User()
        self.assertEqual(var.first_name, "")

    def test_user_last_name(self):
        """ Testing User attributes"""
        var = User()
        self.assertEqual(var.last_name, "")

    def test_user_email(self):
        """ Testing User attributes"""
        var = User()
        self.assertEqual(var.email, "")

    def test_user_password(self):
        """ Testing User attributes"""
        var = User()
        self.assertEqual(var.password, "")
