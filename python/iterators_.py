import itertools


# TODO: itertools module examples

# iterators
# ---------

# an iterator is an object that implements the iterator protocol, which
# consists of the methods __iter__() and __next__().

# "for item in iterable" creates an iterator object from the iterable object
# using iter() and iterates over it using the next() method until a
# StopIteration exception is raised

arr = [1, 2, 3, 4, 5]

## example of built-in iterator
for item in arr:
    print(item)

## is equivalent to
iter_arr = iter(arr)  # calls arr.__iter__()
while True:
    try:
        item = next(iter_arr)  # calls iter_arr.__next__()
        print(item)
    except StopIteration:
        break


# class-based iterators
# ---------------------


class Fib:
    def __init__(self, n):
        self.a = 0
        self.b = 1
        self.n = n
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            current = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return current
        else:
            raise StopIteration


fib_iter = Fib(10)
for num in fib_iter:
    print(num)


# reversible iterators
# --------------------


# an iterator can also implement the __reversed__() method to support
# reversed iteration using the reversed() built-in function


class ReversibleIterator:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            self.i += 1
            return self.i
        else:
            raise StopIteration

    def __reversed__(self):
        return iter(range(self.n, 0, -1))


my_iter2 = ReversibleIterator(10)

print("Forward iteration:")
for item in my_iter2:
    print(item)

print("Reverse iteration:")
for item in reversed(my_iter2):
    print(item)
