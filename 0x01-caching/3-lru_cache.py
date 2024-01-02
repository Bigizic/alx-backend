#!/usr/bin/python3
"""A class LRUCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A LRUCache class inheriting from BaseCaching and
    proceeds to define certain methods
    """

    def __init__(self, dicts={}, count=0):
        """Constructor
        """
        self.dicts = dicts
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

        self.dicts[key] = self.count
        self.count += 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            dicts_min = min(self.dicts.values())
            get_key = [k for k, v in self.dicts.items() if v == dicts_min]
            self.cache_data.pop(get_key[0])
            self.dicts.pop(get_key[0])
            print(f"DISCARD: {get_key[0]}")

    def get(self, key):
        """Retrives the value of a key from self.cache_data
        """
        if key:
            for k, v in self.cache_data.items():
                if k == key:
                    tmp = max(self.dicts.values())
                    self.dicts[key] = tmp + 1
                    self.count += 1
                    return v
        return None
