# stack is a last in first out (LIFO) data structure
# pushing/popping elements is O(1)
# searching for an element is O(n)
# functions calls is managed using a call stack

# stack implementation using deque
from collections import deque

class Stack():
    def __init__(self):
        self.stk = deque()
    
    def push(self, val):
        self.stk.append(val)

    def pop(self):
        self.stk.pop()
    
    def peek(self):
        return self.stk[-1]

    def clear(self):
        self.stk = deque()

    def is_empty(self):
        return len(self.stk) == 0

    def length(self):
        return len(self.stk)


# stack implementation using lists
class Stack():
    def __init__(self):
        self.stk = []
    
    def push(self, val):
        self.stk.append(val)

    def pop(self):
        self.stk.pop()
    
    def peek(self):
        return self.stk[-1]

    def clear(self):
        self.stk = []

    def is_empty(self):
        return len(self.stk) == 0

    def length(self):
        return len(self.stk)