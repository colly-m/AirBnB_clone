#!/usr/bin/python3
"""Defines unittest for Review Class"""

import unittest
import time
import re
import json
import os
from datetime import datetime
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Unittest for Review class"""
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
        """Tests the instantiation of Review class"""
        b = Review()
        self.assertEqual(str(type(b)), "<class 'models.review.Review'>")
        self.assertIsInstance(b, Review)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """
        Tests attributes of Review class
        """
        attributes = storage.attributes()["Review"]
        obj = Review()
        for key, val in attributes.items():
            self.assertTrue(hasattr(obj, key))
            self.assertEqual(type(getattr(obj, key, None)), val)


if __name__ == "__main__":
    unittest.main()
