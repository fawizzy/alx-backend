#!/usr/bin/env python3
"""
BaseCache module
"""
from BaseCache import BaseCaching


class MRUCache(BaseCaching):
    """
    A cache system for most recently used
    """
    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.lru = []

    def put(self, key, item):
        """
        Cache a key-value pair
        """
        if key is None or item is None:
            return

        if key in self.lru:
            del self.lru[self.lru.index(key)]
        self.cache_data[key] = item
        self.lru.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del_key = self.lru[-2]
            del self.cache_data[del_key]
            del self.lru[-2]
            print("DISCARD: ", del_key)

    def get(self, key):
        """
            get the value of the key from the cache
        """
        if key in self.lru:
            del self.lru[self.lru.index(key)]
        if key in list(self.cache_data.keys()):
            self.lru.append(key)

        try:
            return self.cache_data[key]
        except KeyError:
            None
