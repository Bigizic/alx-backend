#!/usr/bin/env python3
"""A class LFUCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Implementation of LEAST FREQUENCY USED ITEM Caching algorithm
    @param(BaseCaching): <BaseCaching class>
    """

    def __init__(self):
        """Constructor
        """
        self.count = 0
        self.access_freq = {}
        self.get_counter = None
        super().__init__()

    def put(self, key, item):
        """Assigns to the dictionary from BaseCaching the 'item' value of the
        key 'key'
        """
        if key is None or item is None:
            pass

        if key and item not in [None]:
            # self.cache_data[key] = item
            if key not in list(self.cache_data.keys()):
                if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                    self.cache_data[key] = item
                    self.access_freq[key] = 1
                else:
                    lfa = min(self.access_freq.values())
                    get_key = [k for k, v in self.access_freq.items()
                               if v == lfa]
                    self.cache_data.pop(get_key[0])
                    self.access_freq.pop(get_key[0])
                    self.cache_data[key] = item
                    self.access_freq[key] = 1
                    print(f"DISCARD: {get_key[0]}")
            else:
                self.cache_data[key] = item
                self.access_freq[key] = 2

    def get(self, key):
        """Retrives the value of a key from self.cache_data
        """
        if key:
            for k, v in self.cache_data.items():
                if k == key:
                    self.access_freq[key] = 2
                    self.get_counter = key
                    return v
        return None
