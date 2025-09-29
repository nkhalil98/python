"""
Queue
"""

from __future__ import annotations

from collections import deque


class Queue:
    def __init__(self, n=None):
        self.q = deque()
        self.size = n if n is not None else float("inf")

    def __len__(self):
        return len(self.q)

    def enqueue(self, val):
        if len(self.q) >= self.size:
            raise QueueFullError()
        self.q.appendleft(val)

    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyError()
        return self.q.pop()

    def clear(self):
        self.q = deque()

    def is_empty(self):
        return len(self.q) == 0


class QueueFullError(Exception):
    pass


class QueueEmptyError(Exception):
    pass
