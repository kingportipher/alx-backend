#!/usr/bin/env python3
"""FIFO caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A caching system that uses FIFO (First-In, First-Out) policy.
    """

    def __init__(self):
        """Initialize the cache with FIFO behavior."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache.

        If the cache exceeds the maximum limit, discard the oldest item.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieve an item from the cache by key.

        Returns None if the key doesn't exist.
        """
        return self.cache_data.get(key)
