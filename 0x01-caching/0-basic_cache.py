#!/usr/bin/env python3
"""
The class BasicCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class inherits from BaseCaching and represents
    a basic cache implementation.
    """

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key of the item.
            item: The item to be added to the cache.
        """
        if key is not None and item is not None:
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
        if key is not None and key in self.cache_data:
            return self.cache_data[key]

        return None
