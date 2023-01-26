#!/usr/bin/env python3
"""
3-lru_cache
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    class LRUCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        initialize class
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del_item = self.cache_data.popitem(last=False)
            print('DISCARD: {}'.format(del_item[0]))

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
