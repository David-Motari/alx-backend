#!/usr/bin/env python3
"""
4-mru_cache
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    class MRUCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        initialize class
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.most_recently_used = ""

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data.update({key: item})
                    self.most_recently_used = key
                else:
                    del_item = self.most_recently_used
                    del self.cache_data[del_item]
                    print('DISCARD: {}'.format(del_item[0]))
                    self.cache_data[key] = item
                    self.most_recently_used = key
            else:
                self.cache_data[key] = item
                self.most_recently_used = key

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key in self.cache_data:
            self.most_recently_used = key
            return self.cache_data.get(key)
