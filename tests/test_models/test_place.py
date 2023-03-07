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
from models.place import Place

class Tests(unittest.TestCase):
    """ Test functions for modules"""

    def test_place_city_id(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.city_id, "")

    def test_place_user_id(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.user_id, "")

    def test_place_name(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.name, "")

    def test_place_description(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.description, "")
        
    def test_place_number_rooms(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.number_rooms, 0)

    def test_place_number_bathrooms(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.number_bathrooms, 0)

    def test_place_max_guests(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.max_guest, 0)

    def test_place_price_night(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.price_by_night, 0)

    def test_place_latitude(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.latitude, 0.0)

    def test_place_longitude(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.longitude, 0.0)

    def test_place_amenity_id(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.amenity_ids, [])
