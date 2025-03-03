"""
Hash Table/Hash Map
"""

from __future__ import annotations


# hash table without collision handling
class HashTable:
    def __init__(self, n=100):  # O(1)
        self.max_size = n
        self.arr = [None for _ in range(n)]

    def get_hash(self, key):  # O(1)
        if isinstance(key, (float, int)):
            return int(key) % self.max_size
        elif isinstance(key, str):
            h = 0
            for char in key:
                h += ord(char)
            return h % self.max_size
        else:
            raise ValueError("Invalid key type")

    def __setitem__(self, key, val):  # O(1)
        hash_value = self.get_hash(key)
        self.arr[hash_value] = val

    def __getitem__(self, key):  # O(1)
        hash_value = self.get_hash(key)
        if self.arr[hash_value] is None:
            raise KeyError(key)
        return self.arr[hash_value]

    def __delitem__(self, key):  # O(1)
        hash_value = self.get_hash(key)
        if self.arr[hash_value] is None:
            raise KeyError(key)
        self.arr[hash_value] = None


# hash table with collision handling using separate chaining
class CHashTable:
    def __init__(self, n):  # O(1)
        self.max_size = n
        self.arr = [[] for _ in range(n)]

    def get_hash(self, key):  # O(1)
        if isinstance(key, (float, int)):
            return int(key) % self.max_size
        elif isinstance(key, str):
            h = 0
            for char in key:
                h += ord(char)
            return h % self.max_size
        else:
            raise ValueError("Invalid key type")

    def __setitem__(self, key, val):  # O(1) average, O(n) worst
        hash_value = self.get_hash(key)

        if not self.arr[hash_value]:
            self.arr[hash_value].append((key, val))
            return

        for index, element in enumerate(self.arr[hash_value]):
            if element[0] == key:
                self.arr[hash_value][index] = (key, val)
                return
        self.arr[hash_value].append((key, val))

    def __getitem__(self, key):  # O(1) average, O(n) worst
        hash_value = self.get_hash(key)

        if not self.arr[hash_value]:
            raise KeyError(key)

        for element in self.arr[hash_value]:
            if element[0] == key:
                return element[1]
        raise KeyError(key)

    def __delitem__(self, key):  # O(1) average, O(n) worst
        hash_value = self.get_hash(key)

        if not self.arr[hash_value]:
            raise KeyError(key)

        for element in self.arr[hash_value]:
            if element[0] == key:
                self.arr[hash_value].remove(element)
                return
        raise KeyError(key)


# TODO: hash table with collision handling using open addressing (linear probing)
