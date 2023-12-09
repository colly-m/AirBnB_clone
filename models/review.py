#!/usr/bin/python3
"""Module for class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A class representaion of review BaseModule"""
    place_id = ''
    user_id = ''
    text = ''
