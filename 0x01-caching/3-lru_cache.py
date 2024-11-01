#!/usr/bin/env python3
"""1-lru_cache module"""
BaseCaching = __import__('base_caching').BaseCaching


class Node:
    def __init__(self, key, item) -> None:
        """ Initiliaze
        """
        self.key = key
        self.item = item
        self.next = None
        self.prev = None


class LRUCache(BaseCaching):
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        # Initialize the linked list with head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

        # Dictionary to store nodes for easy access
        self.node_map = {}

    def remove(self, node):
        """Removes a node from the linked list."""
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

    def insert_at_tail(self, key, item):
        """Inserts a new node at the tail (most recent) position."""
        node = Node(key, item)

        last_node = self.tail.prev
        last_node.next = node
        node.prev = last_node

        node.next = self.tail
        self.tail.prev = node

        # Keep track of the node by key
        self.node_map[key] = node

        return node

    def put(self, key, item):
        """Insert an item in the cache, following LRU policy."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # If the key exists, remove the old node from the linked list
            self.remove(self.node_map[key])
            del self.cache_data[key]

        elif len(self.cache_data) >= LRUCache.MAX_ITEMS:
            # If cache is full, remove the least recently used item
            lru_node = self.head.next
            self.remove(lru_node)
            del self.cache_data[lru_node.key]
            del self.node_map[lru_node.key]
            print(f"DISCARD: {lru_node.key}")

        # Insert the new item at the tail and update cache
        self.insert_at_tail(key, item)
        # Only store the item, not the node
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key and move it to the most recent position."""
        if key in self.cache_data:
            node = self.node_map[key]
            self.remove(node)
            # Move to the end (most recent)
            self.insert_at_tail(node.key, node.item)
            # Return the item from cache_data
            return self.cache_data[key]
        return None
