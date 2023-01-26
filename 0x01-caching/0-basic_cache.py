#!/usr/bin/python3
""" 
0-basic_cache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    class BasicCache that inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key 'key'
        """
        if key == None or item == None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """
        return value of key in self.cache_data
        """
        return self.cache_data.get(key)
