#!/usr/bin/python3
"""Defines unittest for User Class"""

import unittest
import re
import json
from models.user import User
import time
import os
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """Sets up the test method"""
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
        """Tests the instantiation of User class"""
        b = User()
        self.assertEqual(str(type(b)), "<class 'models.user.User'>")
        self.assertIsInstance(b, User)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests attributes of User class"""
        attributes = storage.attributes()["User"]
        obj = User()
        for key, val in attributes.items():
            self.assertTrue(hasattr(obj, key))
            self.assertEqual(type(getattr(obj, key, None)), val)


if __name__ == "__main__":
    unittest.main()
