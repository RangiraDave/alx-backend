#!/usr/bin/env python3
"""
Script to Create the class LIFOCache that inherits from BaseCaching
and is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching class.
    Implements a Last-In-First-Out (LIFO) caching algorithm.
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: Key of the item.
            item: Item to be added to the cache.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_item = list(self.cache_data.keys())[-1]
            del self.cache_data[last_item]
            print("DISCARD:", last_item)

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: Key of the item to be retrieved.

        Returns:
            The item associated with the given key,
            or None if the key is not found in the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
