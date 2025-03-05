"""
Queue
"""

from __future__ import annotations

from collections import deque


# queue implementation using deque
class Queue:
    def __init__(self):  # O(1)
        self.q = deque()

    def enqueue(self, val):  # O(1)
        self.q.appendleft(val)

    def dequeue(self):  # O(1)
        if self.is_empty():
            return None
        return self.q.pop()

    def clear(self):  # O(1)
        self.q = deque()

    def is_empty(self):  # O(1)
        return len(self.q) == 0

    def size(self):  # O(1)
        return len(self.q)


# queue implementation using python list
class LQueue:
    def __init__(self):  # O(1)
        self.q = []

    def enqueue(self, val):  # O(n)
        self.q.insert(0, val)

    def dequeue(self):  # O(1)
        if self.is_empty():
            return None
        return self.q.pop()

    def clear(self):  # O(1)
        self.q = []

    def is_empty(self):  # O(1)
        return len(self.q) == 0

    def size(self):  # O(1)
        return len(self.q)
