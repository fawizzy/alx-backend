#!/usr/bin/env python3
"""
BaseCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Defines a class for caching information in key-value pairs
    Methods:
        put(key, item) - store a key-value pair
        get(key) - retrieve the value associated with a key
    """

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        super().__init__()

    def put(self, key, item):
        """
        Store a key-value pair
        Args:
            Key
            Item
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        get the value of the key from the dictionary
        """
        if key is None:
            return None

        try:
            return self.cache_data[key]
        except KeyError:
            return None
