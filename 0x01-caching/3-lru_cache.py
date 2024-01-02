#!/usr/bin/python3
"""A class LRUCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Implementation of the LEAST RECENTLY USED(LRU) Caching algorithm
    @param (BaseCaching): <BaseCaching class>
    """

    def __init__(self, cache_freq={}, count=0):
        """Constructor
        """
        self.cache_freq = cache_freq
        self.count = count
        super().__init__()

    def put(self, key, item):
        """Assigns to the dictionary from BaseCaching the 'item' value of the
        key 'key'
        """
        if key is None or item is None:
            pass

        if key and item not in [None]:
            self.cache_data[key] = item

        self.cache_freq[key] = self.count
        self.count += 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru = min(self.cache_freq.values())
            get_key = [k for k, v in self.cache_freq.items() if v == lru]
            self.cache_data.pop(get_key[0])
            self.cache_freq.pop(get_key[0])
            print(f"DISCARD: {get_key[0]}")

    def get(self, key):
        """Retrives the value of a key from self.cache_data
        """
        if key:
            for k, v in self.cache_data.items():
                if k == key:
                    tmp = max(self.cache_freq.values())
                    self.cache_freq[key] = tmp + 1
                    self.count += 1
                    return v
        return None
