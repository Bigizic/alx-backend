#!/usr/bin/env python3
"""A class FIFOCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A FIFO caching system
    """

    def __init__(self):
        """Constructor
        """
        super().__init__()

    def put(self, key, item):
        """Assigns to the dictionary from BaseCaching the 'item' value of the
        key 'key'
        """
        if key == None or item == None:
            pass

        if key and item not in [None]:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item = [x for x, v in self.cache_data.items()]
            self.cache_data.pop(first_item[0])
            print(f"DISCARD: {first_item[0]}")

    def get(self, key):
        """Retrives the value of a key from self.cache_data
        """
        if key:
            for k, v in self.cache_data.items():
                if k == key:
                    return v
        return None
