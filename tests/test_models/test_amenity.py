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
from models.amenity import Amenity

class Tests(unittest.TestCase):
    """ Test functions for modules"""

    def test_amenity(self):
        """ Testing amenity attributes """
        var = Amenity()
        self.assertEqual(var.name,"")
