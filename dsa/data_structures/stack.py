"""
Stack (LIFO)
"""

from __future__ import annotations

from collections import deque

from .linked_list import Node


class Stack:
    def __init__(self, max_size=None):
        self.stack = deque()
        self.max_size = max_size

    def __len__(self):
        return len(self.stack)

    def push(self, val):
        if not self.has_space():
            raise StackOverflowError()
        self.stack.append(val)

    def pop(self):
        if self.is_empty():
            raise StackUnderflowError()
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def clear(self):
        self.stack = deque()

    def has_space(self):
        return self.max_size is None or len(self.stack) < self.max_size

    def is_empty(self):
        return len(self.stack) == 0


class LinkedListStack:
    def __init__(self, max_size=None):
        self.head = None  # top
        self.size = 0
        self.max_size = max_size

    def push(self, value):
        if not self.has_space():
            raise StackOverflowError()
        item = Node(value, self.head)
        self.head = item
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise StackUnderflowError()

        item_to_remove = self.head
        self.head = item_to_remove.next
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


class StackOverflowError(Exception):
    pass


class StackUnderflowError(Exception):
    pass
