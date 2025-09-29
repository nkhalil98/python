"""
Hash Table (Hash Map)
    - Without collision handling
    - Collision handling using separate chaining
    - Collision handling using open addressing (linear probing)
"""

from __future__ import annotations


class HashTable:
    def __init__(self, n=100):
        self.max_size = n
        self.arr = [None for _ in range(n)]
        self.keys = []

    def __setitem__(self, key, val):
        hash_value = self._hash(key)
        self.arr[hash_value] = val
        self.keys.append(key)

    def __getitem__(self, key):
        if key not in self.keys:
            raise KeyError(key)
        hash_value = self._hash(key)
        return self.arr[hash_value]

    def __delitem__(self, key):
        if key not in self.keys:
            raise KeyError(key)
        hash_value = self._hash(key)
        self.arr[hash_value] = None
        self.keys.remove(key)

    def __contains__(self, key):
        return key in self.keys

    def __len__(self):
        return len(self.keys)

    def _hash(self, key):
        if isinstance(key, (float, int)):
            return int(key) % self.max_size
        elif isinstance(key, str):
            h = 0
            for char in key:
                h += ord(char)
            return h % self.max_size
        else:
            raise ValueError("Invalid key type")


class CHashTable:
    def __init__(self, n):
        self.max_size = n
        self.arr = [[] for _ in range(n)]
        self.keys = []

    def __setitem__(self, key, val):
        hash_value = self._hash(key)
        bucket = self.arr[hash_value]

        if key in self.keys:
            for i, element in enumerate(bucket):
                if element[0] == key:
                    bucket[i] = (key, val)
                    return
        else:
            bucket.append((key, val))
            self.keys.append(key)

    def __getitem__(self, key):
        if key not in self.keys:
            raise KeyError(key)
        hash_value = self._hash(key)
        bucket = self.arr[hash_value]

        for element in bucket:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        if key not in self.keys:
            raise KeyError(key)
        hash_value = self._hash(key)
        bucket = self.arr[hash_value]

        for element in bucket:
            if element[0] == key:
                bucket.remove(element)
                self.keys.remove(key)
                return

    def __contains__(self, key):
        return key in self.keys

    def __len__(self):
        return len(self.keys)

    def _hash(self, key):
        if isinstance(key, (float, int)):
            return int(key) % self.max_size
        elif isinstance(key, str):
            h = 0
            for char in key:
                h += ord(char)
            return h % self.max_size
        else:
            raise ValueError("Invalid key type")


class OAHashTable:
    def __init__(self, n):
        self.max_size = n
        self.arr = [None for _ in range(n)]
        self.keys = []

    def __setitem__(self, key, val):
        slot = self._find_slot(key)
        self.arr[slot] = (key, val)
        self.keys.append(key)

    def __getitem__(self, key):
        if key not in self.keys:
            raise KeyError(key)
        slot = self._find_slot(key)
        return self.arr[slot][1]

    def __delitem__(self, key):
        if key not in self.keys:
            raise KeyError(key)
        slot = self._find_slot(key)
        self.arr[slot] = None
        self.keys.remove(key)

    def __contains__(self, key):
        return key in self.keys

    def __len__(self):
        return len(self.keys)

    def _hash(self, key):
        if isinstance(key, (float, int)):
            return int(key) % self.max_size
        elif isinstance(key, str):
            h = 0
            for char in key:
                h += ord(char)
            return h % self.max_size
        else:
            raise ValueError("Invalid key type")

    def _find_slot(self, key):
        hash_value = self._hash(key)

        for i in self._linear_probing_range(hash_value):
            if self.arr[i] is None or self.arr[i][0] == key:
                return i
        raise HashTableFullError("Hash Table is full")

    def _linear_probing_range(self, hash_value):
        return range(hash_value, self.max_size) + range(0, hash_value)


class HashTableFullError(Exception):
    pass
