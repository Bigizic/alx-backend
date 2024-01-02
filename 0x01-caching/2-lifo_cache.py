#!/usr/bin/env python3
"""A class LIFOCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A LIFOCache class inheriting from BaseCaching and
    proceeds to define certain methods
    """

    def __init__(self):
        """Constructor
        """
        super().__init__()

    def put(self, key, item):
        """Assigns to the dictionary from BaseCaching the 'item' value of the
        key 'key'
        """
        if key or item in [None]:
            pass

        self.cache_data[key] = item
        lists = [x for x, v in self.cache_data.items()]

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(lists[-2])
            print(f"DISCARD: {lists[-2]}")

    def get(self, key):
        """Retrives the value of a key from self.cache_data
        """
        if key:
            for k, v in self.cache_data.items():
                if k == key:
                    return v
        return None