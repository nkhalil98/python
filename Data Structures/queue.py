# queue is a first in first out (FIFO) data structure
# pushing/popping elements is O(1)
# searching for an element is O(n)
# queue is used in multithreaded applications and in designing ordering systems (stock market, store, ...etc)

# queue implementation using deque
from collections import deque

class Queue():
    def __init__(self):
        self.q = deque()
    
    def enqueue(self, val):
        self.q.appendleft(val)

    def dequeue(self):
        self.q.pop()

    def clear(self):
        self.q = deque()

    def peek(self):
        return self.q[-1]

    def is_empty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)


# queue implementation using lists
class LQueue():
    def __init__(self):
        self.q = []
    
    def push(self, val):
        self.q.insert(0, val)

    def pop(self):
        self.q.pop()
    
    def peek(self):
        return self.q[-1]

    def clear(self):
        self.q = []

    def is_empty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)