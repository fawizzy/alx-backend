#!/usr/bin/env python3
"""
    BaseCaching module
"""
from BaseCache import BaseCaching


class FIFOCache(BaseCaching):
    """
        FIFO cache for a FIFO caching system
    """
    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
    
    def put(self, key, item):
        """
            Cache a key value pair
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del_key = list(self.cache_data.keys())[0]
            del self.cache_data[del_key]
            print("DISCARD: ", del_key)

    def get(self, key):
        """
            Return the value of the key from the dictionary
        """
        try:
            self.cache_data[key]
        except:
            None