#!/usr/bin/env python3
"""
Module for a basic caching system.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A class that allows storing and retrieving items
    from a cache using a dictionary.
    """
    
    def put(self, key, item):
        """Stores an item in the cache.

        If either the key or item is None, this method does nothing.
        Otherwise, it stores the item in the cache with the given key.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache by its key.

        If the key is None or does not exist in the cache, 
        this method returns None. Otherwise, it returns the
        value associated with the key.
        """
        return self.cache_data.get(key)

