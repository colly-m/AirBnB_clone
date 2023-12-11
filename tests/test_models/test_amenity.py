#!/usr/bin/python3
"""test for the amenity model"""


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models import storage
import time
import re
import json
import os


class TestAmenity(unittest.TestCase):
    """Unittest for Amenity class"""
    def setUp(self):
        """Sets up the test methods"""
        pass

    def tearDown(self):
        """Tears down the test methods"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets the FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests the instantiation of Amenity class"""
        b = Amenity()
        self.assertEqual(str(type(b)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(b, Amenity)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests attributes of Amenity class"""
        attributes = storage.attributes()["Amenity"]
        obj = Amenity()
        for key, val in attributes.items():
            self.assertTrue(hasattr(obj, key))
            self.assertEqual(type(getattr(obj, key, None)), val)


if __name__ == "__main__":
    unittest.main()
