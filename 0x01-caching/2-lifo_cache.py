#!/usr/bin/env python3
"""
BaseCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
        Cache system for  LIFO caching
    """
    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Cache a key-value pair
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del_key = self.order[-2]
            del self.cache_data[del_key]
            del self.order[-2]
            print(self.order)
            print("DISCARD: ", del_key)

    def get(self, key):
        """
        Return the value linked to a given key, or None
        """
        try:
            return self.cache_data[key]
        except KeyError:
            None
