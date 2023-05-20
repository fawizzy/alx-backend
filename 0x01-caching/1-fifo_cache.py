#!/usr/bin/env python3
"""
FIFO caching
"""
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching system that inherits from BaseCaching class.
    It implements a caching system using the First-In-First-Out (FIFO) algorithm.
    """

    def __init__(self):
        """
        Initializes an instance of FIFOCache.

        Args:
            None

        Returns:
            None
        """
        super().__init__()

    def put(self, key, item):
        """
        Inserts an item into the cache with the specified key.

        If the key or item is None, this method does nothing.
        If the number of items in the cache exceeds the maximum limit (BaseCaching.MAX_ITEMS),
        it discards the first item put in the cache based on the FIFO algorithm.

        Args:
            key: The key to associate the item with.
            item: The item to be stored in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Get the first item (oldest) in the cache
            first_item = next(iter(self.cache_data))
            # Remove the first item from the cache
            del self.cache_data[first_item]
            print("DISCARD:", first_item)

        # Assign the item value to the key in the cache
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value associated with the specified key from the cache.

        If the key is None or does not exist in the cache, it returns None.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key in the cache, or None if the key is None or not found.
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
