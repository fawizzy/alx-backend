#!/usr/bin/env python3
"""
BaseCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO caching system
    """
    def __init__(self):
        """
        Initialize the class
        """
        super().__init__()
        self.sequence = []

    def put(self, key, item):
        """
        Cache a key-value
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.sequence.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_in = self.sequence[-2]
            del self.cache_data[last_in]
            del self.sequence[-2]
            print("DISCARD: ", last_in)

    def get(self, key):
        """
        Return the value linked to a given key, or None
        """
        if key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
