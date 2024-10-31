#!/usr/bin/env python3
"""1-lifo_cache module"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """BasicCache class that inherits from BaseCaching.

    This class implements a simple caching system.
    """
    def __init__(self):
        """Initialize the BasicCache instance.

        Calls the parent class's __init__ method to initialize
        cache_data.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache.

        Args:
            key: The key under which the item is stored.
            item: The item to be stored in the cache.

        If either key or item is None, the method does nothing.
        """
        if not key or not item:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
            self.order.append(key)

        else:
            if len(self.cache_data) >= LIFOCache.MAX_ITEMS:
                print(self.order)
                lastin = self.order[-1]
                del self.cache_data[lastin]
                print("DISCARD: {}".format(lastin))
                self.order.remove(lastin)

            self.cache_data[key] = item
            self.order.append(key)

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
        return self.cache_data.get(key)
