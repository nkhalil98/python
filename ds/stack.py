"""
Stack
"""

from __future__ import annotations

from collections import deque


# stack implementation using deque
class Stack:
    def __init__(self):
        self.stk = deque()

    def push(self, val):
        self.stk.append(val)

    def pop(self):
        if self.is_empty():
            return None
        return self.stk.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stk[-1]

    def clear(self):
        self.stk = deque()

    def is_empty(self):
        return len(self.stk) == 0

    def size(self):
        return len(self.stk)


# stack implementation using python list
class LStack:
    def __init__(self):
        self.stk = []

    def push(self, val):
        self.stk.append(val)

    def pop(self):
        if self.is_empty():
            return None
        return self.stk.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stk[-1]

    def clear(self):
        self.stk = []

    def is_empty(self):
        return len(self.stk) == 0

    def size(self):
        return len(self.stk)
