#!/usr/bin/env python3
""" Basic Cache module
This module contains a BasicCache class that
implements a simple caching system.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache inherits from BaseCaching.
    It implements a caching system without limits on the number of items.
    """

    def put(self, key, item):
        """ Add an item to the cache.

        Args:
            key: The key under which the item is stored.
            item: The value to be stored in the cache.

        If key or item is None, do nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache by key.

        Args:
            key: The key for the item to be retrieved.

        Returns:
            The value associated with the key,
            or None if the key doesn't exist.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
