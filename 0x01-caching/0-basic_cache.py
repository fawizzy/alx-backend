#!/usr/bin/env python3
"""
BaseCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    class for caching information in key-value pairs
    """

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        super().__init__()

    def put(self, key, item):
        """
        Store a key-value pair
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

        if key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
