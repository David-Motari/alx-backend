#!/usr/bin/env python3
"""
1-fifo_cache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    class FIFOCache that inherits from BaseCaching and is a caching system
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
        if key is None and item is None:
            pass
        else:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del_item = sorted(self.cache_data)[0]
            self.cache_data.pop(del_item)
            print("DISCARD: {}".format(del_item))

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        return self.cache_data.get(key)
