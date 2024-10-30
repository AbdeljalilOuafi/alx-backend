#!/usr/bin/env python3
"""0-basic_cache module"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class that inherits from BaseCaching.

    This class implements a simple caching system.
    """
    
    def __init__(self):
        """Initialize the BasicCache instance.

        Calls the parent class's __init__ method to initialize
        cache_data.
        """
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache.

        Args:
            key: The key under which the item is stored.
            item: The item to be stored in the cache.

        If either key or item is None, the method does nothing.
        """
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key if it exists,
            otherwise None.
        """
        if key is None:
            return None
        try:
            value = self.cache_data[key]
            return value
        except KeyError:
            return None
