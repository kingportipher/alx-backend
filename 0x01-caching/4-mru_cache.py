#!/usr/bin/env python3
"""MRU caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU (Most Recently Used) caching system.
    """

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache.

        Discard the most recently used item if cache exceeds limit.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            mru_key, _ = self.cache_data.popitem(last=True)
            print("DISCARD:", mru_key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item by key."""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
