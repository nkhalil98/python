"""
Queue
"""

from __future__ import annotations

from collections import deque


# queue implementation using deque
class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, val):
        self.q.appendleft(val)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.q.pop()

    def clear(self):
        self.q = deque()

    def is_empty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)


# queue implementation using python list
class LQueue:
    def __init__(self):
        self.q = []

    def enqueue(self, val):
        self.q.insert(0, val)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.q.pop()

    def clear(self):
        self.q = []

    def is_empty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)
