#!/usr/bin/env python3
"""LIFO caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Caching system with LIFO (Last-In, First-Out) removal policy.
    """

    def __init__(self):
        """Initialize the cache with LIFO behavior."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache.

        If the cache exceeds the max limit, discard the last added item.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            last_key, _ = self.cache_data.popitem(last=True)
            print("DISCARD:", last_key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache by key.

        Returns None if the key doesn’t exist.
        """
        return self.cache_data.get(key)
