#!/usr/bin/env python3
"""LRU caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Caching system with LRU (Least Recently Used) removal policy.
    """

    def __init__(self):
        """Initialize the cache with LRU behavior."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache.

        If the cache exceeds the max limit, discard the least recently used item.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", lru_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """Retrieve an item from the cache by key.

        Updates the item's position as most recently used.
        Returns None if the key doesn’t exist.
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key)
