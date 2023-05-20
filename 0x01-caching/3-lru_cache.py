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
        self.order = []

    def put(self, key, item):
        """
        add key-value pair to the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            least_recently_used = self.order.pop(0)
            del self.cache_data[least_recently_used]
            print("DISCARD:", least_recently_used)
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        get the value of the key from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
