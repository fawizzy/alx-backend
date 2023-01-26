#!/usr/bin/env python3
"""
BaseCache module
"""

from BaseCache import BaseCaching


class BasicCache(BaseCaching):
    """
        A Basic cache system
    """

    def __init__(self):
        """
        INnitialise the system
        """
        super().__init__()

    def put(self, key, item):
        if key is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        get the value of the key from the dictionary
        """
        if key is None:
            return

        try:
            return self.cache_data[key]
        except KeyError:
            return None
