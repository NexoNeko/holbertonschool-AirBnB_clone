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
from models.review import Review


class Tests(unittest.TestCase):
    """ Test functions for modules"""

    def test_review_place_id(self):
        """ Testing Review attributes """
        var = Review()
        self.assertEqual(var.place_id, "")

    def test_review_user_id(self):
        """ Testing Review attributes """
        var = Review()
        self.assertEqual(var.user_id, "")

    def test_review_text(self):
        """ Testing Review attributes """
        var = Review()
        self.assertEqual(var.text, "")
