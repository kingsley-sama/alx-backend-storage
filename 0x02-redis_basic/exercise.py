#!/usr/bin/python3
"""This module defines the exercise.py class."""
import redis
import uuid
from typing import Union


class Cache:
    """Create a store method that takes a data argument and returns a string"""
    def __init__(self):
        self._redis = redis.Redis()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method that takes a data argument and returns a string"""
        id = uuid.uuid4().__str__()
        self._redis.set(id, data)

        return id
