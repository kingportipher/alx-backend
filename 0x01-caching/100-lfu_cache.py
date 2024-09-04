#!/usr/bin/env python3
"""Least Frequently Used caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU (Least Frequently Used) caching system.
    """

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def __reorder_items(self, key):
        """Reorder items by frequency and recency."""
        for i, (k, freq) in enumerate(self.keys_freq):
            if k == key:
                self.keys_freq.pop(i)
                self.keys_freq.insert(0, (key, freq + 1))
                break

    def put(self, key, item):
        """Add an item to the cache.

        Discard the least frequently used item if cache exceeds limit.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard least frequently used or least recently used if frequencies match
            lfu_key, _ = self.keys_freq.pop()
            del self.cache_data[lfu_key]
            print("DISCARD:", lfu_key)

        self.cache_data[key] = item

        if key not in [k for k, _ in self.keys_freq]:
            self.keys_freq.append((key, 1))
        else:
            self.__reorder_items(key)

    def get(self, key):
        """Retrieve an item by key."""
        if key is None or key not in self.cache_data:
            return None
        self.__reorder_items(key)
        return self.cache_data.get(key)
