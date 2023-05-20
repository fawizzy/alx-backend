#!/usr/bin/env python3
"""
Least recently use caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Least recently used caching system
    """
    def __init__(self):
        """
        Initialize the class
        """
        super().__init__()

    def put(self, key, item):
        """
        add key-value pair to the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least_recently_used = list(self.cache_data.keys())[0]
            del self.cache_data[least_recently_used]
            print("DISCARD: ", least_recently_used)
        self.cache_data[key] = item

    def get(self, key):
        """
        get the value of the key from the cache
        """
        if key in self.lru:
            del self.lru[self.lru.index(key)]
        if key in list(self.cache_data.keys()):
            self.lru.append(key)

        if key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
