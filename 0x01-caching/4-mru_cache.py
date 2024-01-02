#!/usr/bin/env python3
"""A class MRUCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Implementation of the MOST RECENTLY USED Caching algorithm
    @param (BaseCaching): <BaseCaching class>
    """

    def __init__(self, count=0, dicts={}):
        """Constructor
        """
        self.dicts = dicts
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
            self.dicts[key] = self.count + 1
            self.count += 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.get_counter:
                self.cache_data.pop(self.get_counter)
                self.dicts.pop(self.get_counter)
                print(f"DISCARD: {self.get_counter}")
                self.get_counter = None
            else:
                dicts_m = list(self.dicts.keys())
                self.cache_data.pop(dicts_m[-2])
                self.dicts.pop(dicts_m[-2])
                print(f"DISCARD: {dicts_m[-2]}")

    def get(self, key):
        """Retrives the value of a key from self.cache_data
        """
        if key:
            for k, v in self.cache_data.items():
                if k == key:
                    tmp = max(self.dicts.values())
                    self.dicts[key] = tmp + 1
                    self.get_counter = key
                    return v
        return None
