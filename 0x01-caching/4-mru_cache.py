#!/usr/bin/env python3
"""
MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    A cache system for Most Recently Used (MRU) algorithm
    """
    def __init__(self):
        """
        Initialize the MRUCache class by calling the parent's init method
        """
        super().__init__()
        self.mru = []

    def put(self, key, item):
        """
        Cache a key-value pair using the Most Recently Used (MRU) algorithm
        """
        if key is None or item is None:
            return

        if key in self.mru:
            del self.mru[self.mru.index(key)]
        self.cache_data[key] = item
        self.mru.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            most_recently_used = self.mru[-2]
            del self.cache_data[most_recently_used]
            del self.mru[-2]
            print("DISCARD:", most_recently_used)

    def get(self, key):
        """
        Get the value associated with the given key from the cache
        """
        if key in self.mru:
            del self.mru[self.mru.index(key)]
        if key in list(self.cache_data.keys()):
            self.mru.append(key)

        if key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
