#!/usr/bin/env python3
"""
Module for a basic caching system.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A class that allows storing and retrieving items
    """
    
    def put(self, key, item):
        """Stores an item in the cache.

        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache by its key.

        """
        return self.cache_data.get(key)

