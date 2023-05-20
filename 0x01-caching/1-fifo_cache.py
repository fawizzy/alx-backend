#!/usr/bin/env python3
"""
    Fifo cache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
        FIFO caching system
    """
    def __init__(self):
        """
        initialize class parent's init method
        """
        super().__init__()

    def put(self, key, item):
        """
            Cache a key value
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            first_in = list(self.cache_data.keys())[0]
            del self.cache_data[first_in]
            print("DISCARD: ", first_in)
        self.cache_data[key] = item

    def get(self, key):
        """
            Return the value of the key from the dictionary
        """
        if key is None:
            return None

        if key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
