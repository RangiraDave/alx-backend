#!/usr/bin/env python3
"""
Module for implementing a First-In-First-Out (FIFO) cache.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Class that represents a First-In-First-Out (FIFO) cache.
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key of the item.
            item: The item to be added.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the first item in the cache
            first_item = next(iter(self.cache_data))
            # Remove the first item from the cache
            del self.cache_data[first_item]
            print("DISCARD:", first_item)

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key,
            or None if the key is not found in the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
