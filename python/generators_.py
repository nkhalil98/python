import sys
from collections.abc import Generator

# generators
# -----------


## function-based generators


### finite generators
def my_generator(n):
    i = 0
    while i < n:
        yield i
        i += 1


gen = my_generator(10)
for i in gen:
    print(i)

# is equivalent to
gen = my_generator(10)
while True:
    try:
        value = next(gen)
        print(value)
    except StopIteration:
        break


### infinite generators
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fib()
for i in fib_gen:
    print(i)
    if i > 10:
        break


## class-based generators
class Fib(Generator):
    def __init__(self):
        self.a, self.b = 0, 1

    def send(self, ignored_arg):
        return_value = self.a
        self.a, self.b = self.b, self.a + self.b
        return return_value

    def throw(self, type=None, value=None, traceback=None):
        raise StopIteration


fib_gen = Fib()
for i in fib_gen:
    print(i)
    if i > 10:
        break


## generator expressions
gen_expr = (i for i in range(10))
for i in gen_expr:
    print(i)


# advantages of generators
# ------------------------

# generators are memory efficient because they generate values one at a time
# while still remembering their state between values

ten_million_arr = list(range(10_000_000))  # uses a lot of memory to store all values
print(f"List size: {sys.getsizeof(ten_million_arr)} bytes")

y = (i for i in range(10_000_000))  # uses very little memory
print(f"Generator size: {sys.getsizeof(y)} bytes")

# chaining generators using yield from
# ------------------------------------

num_gen = (i for i in range(5))
char_gen = (c for c in "abc")


def combined_generator():
    print("Numbers:")
    yield from num_gen
    print("Characters:")
    yield from char_gen


for item in combined_generator():
    print(item)
