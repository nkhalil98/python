"""
Queue (FIFO)
"""

from __future__ import annotations

from collections import deque

from .linked_list import Node


class Queue:
    def __init__(self, max_size=None):
        self.queue = deque()
        self.max_size = max_size

    def __len__(self):
        return len(self.queue)

    def enqueue(self, val):
        if not self.has_space():
            raise QueueOverflowError()
        self.queue.appendleft(val)

    def dequeue(self):
        if self.is_empty():
            raise QueueUnderflowError()
        return self.queue.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[-1]

    def clear(self):
        self.queue = deque()

    def has_space(self):
        return self.max_size is None or len(self.queue) < self.max_size

    def is_empty(self):
        return len(self.queue) == 0


class LinkedListQueue:
    def __init__(self, max_size=None):
        self.head = None  # front
        self.tail = None  # back
        self.size = 0
        self.max_size = max_size

    def enqueue(self, value):
        if not self.has_space():
            raise QueueOverflowError()

        item_to_add = Node(value)
        if self.is_empty():
            self.head = item_to_add
            self.tail = item_to_add
        else:
            self.tail.next = item_to_add
            self.tail = item_to_add
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise QueueUnderflowError()

        item_to_remove = self.head
        if self.get_size() == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1

        return item_to_remove.val

    def peek(self):
        if self.is_empty():
            return None
        return self.head.val

    def has_space(self):
        if self.max_size is None:
            return True
        return self.max_size > self.size

    def is_empty(self):
        return self.size == 0


class QueueOverflowError(Exception):
    pass


class QueueUnderflowError(Exception):
    pass
