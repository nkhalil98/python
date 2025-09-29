"""
Stack
"""

from __future__ import annotations

from collections import deque


class Stack:
    def __init__(self, n=None):
        self.stk = deque()
        self.size = n if n is not None else float("inf")

    def __len__(self):
        return len(self.stk)

    def push(self, val):
        if len(self.stk) >= self.size:
            raise StackOverflowError()
        self.stk.append(val)

    def pop(self):
        if self.is_empty():
            raise StackUnderflowError()
        return self.stk.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stk[-1]

    def clear(self):
        self.stk = deque()

    def is_empty(self):
        return len(self.stk) == 0


class StackOverflowError(Exception):
    pass


class StackUnderflowError(Exception):
    pass
