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
from models.state import State


class Tests(unittest.TestCase):
    """ Test functions for modules"""

    def test_state(self):
        """ Testing State attributes """
        var = State()
        self.assertEqual(var.name, "")
