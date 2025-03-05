"""
Stack
"""

from __future__ import annotations

from collections import deque


# stack implementation using deque
class Stack:
    def __init__(self):  # O(1)
        self.stk = deque()

    def push(self, val):  # O(1)
        self.stk.append(val)

    def pop(self):  # O(1)
        if self.is_empty():
            return None
        return self.stk.pop()

    def peek(self):  # O(1)
        if self.is_empty():
            return None
        return self.stk[-1]

    def clear(self):  # O(1)
        self.stk = deque()

    def is_empty(self):  # O(1)
        return len(self.stk) == 0

    def size(self):  # O(1)
        return len(self.stk)


# stack implementation using python list
class LStack:
    def __init__(self):  # O(1)
        self.stk = []

    def push(self, val):  # O(1)
        self.stk.append(val)

    def pop(self):  # O(1)
        if self.is_empty():
            return None
        return self.stk.pop()

    def peek(self):  # O(1)
        if self.is_empty():
            return None
        return self.stk[-1]

    def clear(self):  # O(1)
        self.stk = []

    def is_empty(self):  # O(1)
        return len(self.stk) == 0

    def size(self):  # O(1)
        return len(self.stk)
