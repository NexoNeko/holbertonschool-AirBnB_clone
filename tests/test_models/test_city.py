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
from models.city import City

class Tests(unittest.TestCase):
    """ Test functions for modules"""

    def test_city_state_id(self):
        """ Testing City attributes """
        var = City()
        self.assertEqual(var.state_id, "")

    def test_city_name(self):
        """ Testing City attributes """
        var = City()
        self.assertEqual(var.name, "")
