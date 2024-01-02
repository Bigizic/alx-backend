#!/usr/bin/env python3
"""A class MRUCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Implementation of the MOST RECENTLY USED(MRU) Caching algorithm
    @param (BaseCaching): <BaseCaching class>
    """

    def __init__(self, count=0, cache_freq={}):
        """Constructor
        """
        self.cache_freq = cache_freq
        self.count = count
        self.get_counter = None
        super().__init__()

    def put(self, key, item):
        """Assigns to the dictionary from BaseCaching the 'item' value of the
        key 'key'
        """
        if key is None or item is None:
            pass

        if key and item not in [None]:
            self.cache_data[key] = item
            self.cache_freq[key] = self.count + 1
            self.count += 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.get_counter:
                self.cache_data.pop(self.get_counter)
                self.cache_freq.pop(self.get_counter)
                print(f"DISCARD: {self.get_counter}")
                self.get_counter = None
            else:
                mru = list(self.cache_freq.keys())
                self.cache_data.pop(mru[-2])
                self.cache_freq.pop(mru[-2])
                print(f"DISCARD: {mru[-2]}")

    def get(self, key):
        """Retrives the value of a key from self.cache_data
        """
        if key:
            for k, v in self.cache_data.items():
                if k == key:
                    tmp = max(self.cache_freq.values())
                    self.cache_freq[key] = tmp + 1
                    self.get_counter = key
                    return v
        return None
