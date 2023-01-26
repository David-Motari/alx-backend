#!/usr/bin/env python3
"""
2-lifo_cache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    class LIFOCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        initialize class
        """
        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.del_item)
            print('DISCARD:', self.del_item)
        if key is not None:
            self.del_item = key

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        return self.cache_data.get(key)
