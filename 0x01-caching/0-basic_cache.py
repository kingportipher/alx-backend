#!/usr/bin/python3

class BaseCaching:
    def __init__(self):
        """Initialize the cache data dictionary"""
        self.cache_data = {}

class BasicCache(BaseCaching):
    def put(self, key, item):
        """Assign the item value to the dictionary for the given key"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to the key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
