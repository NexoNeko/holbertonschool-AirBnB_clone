#!/usr/bin/python3
"""unittests for base_model.py"""
import unittest
from models.base_model import BaseModel
from models import storage


class tests_base(unittest.TestCase):

    def test_string(self):
        """ Testing manual name setup for
        attribute """
        my_model = BaseModel()
        my_model.name = "Something"
        self.assertEqual(my_model.name, "Something")

    def test_timestamp_create(self):
        """ Testing timestamp creation """
        my_model = BaseModel()
        self.assertIsNotNone(my_model.created_at)

    def test_timestamp_update(self):
        """ Testing timestamp update on save """
        my_model = BaseModel()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_dict(self):
        """ Testing to dictionary function correct
        type"""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertEqual(str(type(my_model_dict)), "<class 'dict'>")

    def test_recreation(self):
        """ Testing recreation of base model
        from saved json """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_model.name, my_new_model.name)

    def test_recreation_datetype(self):
        """ Testing recreation of base model from
        saved json, timestamp """
        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        print(type(my_model.created_at))
        print(type(my_new_model.created_at))
        self.assertEqual(type(my_model.created_at),type(my_new_model.created_at))

    def test_id(self):
        """ Testing if IDs are unique """
        my_model = BaseModel()
        my_model_a = BaseModel()
        self.assertNotEqual(my_model.id, my_model_a.id)

if __name__ == "__main__":
    unittest.main()
