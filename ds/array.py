"""
Array
    - Static Array
    - Dynamic Array
"""

from __future__ import annotations


class StaticArray:
    def __init__(self):  # O(1)
        self.arr = []
        self.size = 0

    def __len__(self):  # O(1)
        return self.size

    def __iter__(self):  # O(n)
        yield from self.arr

    def build(self, data):  # O(n)
        self.arr = [item for item in data]
        self.size = len(self.arr)

    def get_at(self, i):  # O(1)
        if i < 0 or i >= self.size:
            raise IndexError()
        return self.arr[i]

    def set_at(self, i, x):  # O(1)
        if i < 0 or i >= self.size:
            raise IndexError()
        self.arr[i] = x

    def _copy_forward(self, i, n, A, j):  # O(n)
        for k in range(n):
            A[j + k] = self.arr[i + k]

    def _copy_backward(self, i, n, A, j):  # O(n)
        for k in range(n - 1, -1, -1):
            A[j + k] = self.arr[i + k]

    def insert_at(self, i, x):  # O(n)
        n = len(self)
        A = [None] * (n + 1)
        self._copy_forward(0, i, A, 0)
        A[i] = x
        self._copy_forward(i, n - i, A, i + 1)
        self.build(A)

    def delete_at(self, i):  # O(n)
        n = len(self)
        A = [None] * (n - 1)
        self._copy_forward(0, i, A, 0)
        x = self.arr[i]
        self._copy_forward(i + 1, n - i - 1, A, i)
        self.build(A)
        return x

    def insert_first(self, x):  # O(n)
        self.insert_at(0, x)

    def delete_first(self):  # O(n)
        return self.delete_at(0)

    def insert_last(self, x):  # O(n)
        self.insert_at(len(self), x)

    def delete_last(self):  # O(n)
        return self.delete_at(len(self) - 1)


class DynamicArray(StaticArray):
    def __init__(self, r=2):  # O(1)
        super().__init__()
        self.size = 0
        self.r = r
        self._compute_bounds()
        self._resize(0)

    def __len__(self):  # O(1)
        return self.size

    def __iter__(self):  # O(n)
        for i in range(len(self)):
            yield self.arr[i]

    def build(self, data):  # O(n)
        for item in data:
            self.insert_last(item)

    def _compute_bounds(self):  # O(1)
        self.upper = len(self.arr)
        self.lower = len(self.arr) // (self.r * self.r)

    def _resize(self, n):  # O(1) or O(n)
        if self.lower < n < self.upper:
            return
        m = max(n, 1) * self.r
        A = [None] * m
        self._copy_forward(0, self.size, A, 0)
        self.arr = A
        self._compute_bounds()

    def insert_last(self, x):  # O(1) amortized
        self._resize(self.size + 1)
        self.arr[self.size] = x
        self.size += 1

    def delete_last(self):  # O(1) amortized
        self.arr[self.size - 1] = None
        self.size -= 1
        self._resize(self.size)

    def insert_at(self, i, x):  # O(n)
        self.insert_last(None)
        self._copy_backward(i, self.size - (i + 1), self.arr, i + 1)
        self.arr[i] = x

    def delete_at(self, i):  # O(n)
        x = self.arr[i]
        self._copy_forward(i + 1, self.size - (i + 1), self.arr, i)
        self.delete_last()
        return x

    def insert_first(self, x):  # O(n)
        self.insert_at(0, x)

    def delete_first(self):  # O(n)
        return self.delete_at(0)
