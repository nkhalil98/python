from functools import partial, reduce
import inspect


# TODO: function introspection at runtime examples
# TODO: functional programming examples
# TODO: recursion (and function call stack) examples


# functions
# ---------

# function are used to write DRY (don't repeat yourself) code
# functions are black boxes: inputs -> function -> outputs
# functions are interfaces
# python built-in functions: https://docs.python.org/3/library/functions.html


# function definition and calling
# -------------------------------

## function definition


# fmt: off
def my_function(a, b):  # function header (def keyword + name + parameters)
    """
    This is a docstring. It is used to document the function.

    This function takes two parameters, a and b, and returns their sum.
    """
    # function body
    result = a + b

    return result  # return value
# fmt: on


## function signature (function header with type hints for parameters and return value)
def my_second_function(a: int, b: int) -> int:
    pass


## a function can have no parameters and no return value (returns None by default)
def greet():
    print("Hello")


## function calling
greet()  # equivalent to greet.__call__()


## functions can return multiple values by returning a tuple
def add_sub(x, y):
    return x + y, x - y


a, b = add_sub(2, 1)  # unpacking the returned tuple


# function arguments
# ------------------

# parameters vs arguments: parameters are variables in the function definition,
# arguments are the actual values passed to the function when calling it.


## positional arguments
def add(x, y):
    return x + y


sum1 = add(1, 2)  # x=1, y=2

## keyword arguments
sum2 = add(y=2, x=1)  # x=1, y=2


# add(1, 2), add(x=1, y=2), add(y=2, x=1) are equivalent function calls


## optional/default arguments (must come after all positional arguments)


def add2(x, y, z=0):  # z is optional and defaults to 0
    return x + y + z


x1 = add2(1, 2)
x2 = add2(1, 2, 3)


## enforcing positional and keyword arguments
def func(a, b, /, c, d, *, e, f, g=0):
    return a + b + c + d + e + f + g


# a and b are positional-only (they come before the /)
# c and d can be either positional or keyword
# e and f are keyword-only (they come after the *)
# g is an optional keyword-only argument with default value 0
result = func(1, 2, 3, d=4, e=5, f=6, g=7)


## passing an arbitrary number of arguments
def add_nums(*args):  # *args is a tuple
    return sum(args)


sum1 = add_nums(1, 2, 3, 4, 5)
sum2 = add_nums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


## passing an arbitrary number of keyword arguments
def parse_id(**kwargs):  # **kwargs is a dictionary
    for k, v in kwargs.items():
        print(k, v)


parse_id(id=0, name="Nabil", age=26)


## mutable vs immutable arguments (pass by reference vs pass by value)


# functions can modify mutable objects (lists, dictionaries, etc.) passed as
# arguments inplace, but cannot modify immutable objects (integers, strings,
# tuples, etc.)

# to avoid modifying the original mutable object, pass a copy of it (e.g., using
# slicing for lists) when calling the function.


### mutable arguments
def square(arr):
    for index, value in enumerate(arr):
        arr[index] = value**2


arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
square(arr1)  # arr1 = [1, 4, 9]
square(arr2[:])  # arr2 = [4, 5, 6]

### immutable arguments
a = 1


def add_one(x):
    x += 1
    return x


b = add_one(a)  # a = 1, b = 2


### mutable default arguments


# default mutable arguments can lead to unexpected behavior because the default
# value is evaluated only once at function definition time, not each time the
# function is called. Thus, if the mutable object is modified, the modified
# object will be used as the default value in subsequent calls to the function


def append_to_list(value, arr=[]):
    arr.append(value)
    return arr


list1 = append_to_list(1)  # [1]
list2 = append_to_list(2)  # [1, 2]


#### fix 1: use None as default argument
def append_to_list_fixed(value, arr=None):
    if arr is None:
        arr = []
    arr.append(value)
    return arr


list1_fixed = append_to_list_fixed(1)  # [1]
list2_fixed = append_to_list_fixed(2)  # [2]


#### fix 2: use immutable default argument
def append_to_list_fixed_2(value, arr=()):
    arr = list(arr)  # convert tuple to list
    arr.append(value)
    return arr


list1_fixed_2 = append_to_list_fixed_2(1)  # [1]
list2_fixed_2 = append_to_list_fixed_2(2)  # [2]


# lambda/anonymous functions
# --------------------------

# lambda functions are small anonymous functions defined using the `lambda`
# keyword. They can take any number of arguments but can only have one
# expression. They are often used as arguments to higher-order functions
# (functions that take other functions as arguments or return functions)

square = lambda x: x**2  # noqa
print(square.__name__)  # <lambda>
print(square(5))  # 25


# function scoping
# ----------------

# variables defined inside a function are local (cannot be accessed from
# outside). However, the function can still access (but not modify) the value of
# a variable defined outside the function

# use the `nonlocal` keyword to allow a function to modify a variable in the
# nearest enclosing scope (not global scope)

# use the `global` keyword to allow a function to modify a global variable


# namespaces
# types of namespaces: built-in, global, local

# built-in namespace
print(dir(__builtins__))

# global namespace
x = 10


def foo():
    # local namespace
    y = 20
    print("Inside foo:")
    print("Local namespace:", locals().keys())  # or dir()
    print("Global namespace:", globals().keys())
    print("Built-in namespace:", dir(__builtins__))
    print("x =", x)
    print("y =", y)


# scope resolution: LEGB (Local, Enclosing, Global, Built-in)
y = 0


def foo():  # noqa
    x = 1

    def bar():
        print(x)  # will look for x in enclosing scope
        # x = 2  # UnboundLocalError without nonlocal

    bar()


foo()


def foo():
    x = 1

    def bar():
        nonlocal x  # declare x as nonlocal to modify it
        x = 2  # modifies x in enclosing scope
        print(x)

    bar()


foo()


def foo():
    print(y)
    # y += 1  # UnboundLocalError without global


foo()


def foo():
    global y
    print(y)
    y += 1  # modifies global y
    print(y)


foo()

# scope resolution examples
z = 1


def outer():
    z = 2  # noqa

    def inner():
        z = 3
        print(z)  # prints 3

    inner()


outer()


def outer():
    z = 2

    def inner():
        print(z)  # prints 2

    inner()


outer()


def outer():
    def inner():
        print(z)  # prints 1

    inner()


outer()


# functions as first-class objects
# --------------------------------


def square(x):
    return x**2


# assign function to a variable
f = square
print(f(5))


# pass function as an argument to another function
def apply_func(func, x):  # apply_func is a higher-order function
    return func(x)


print(apply_func(square, 6))


# return function from another function
def get_multiplier(factor):
    def multiply(x):
        return x * factor

    return multiply


double = get_multiplier(2)
print(double(7))


# store functions in data structures
funcs = [square, double]
for func in funcs:
    print(func(10))


# higher-order functions
# ----------------------


# higher-order functions are functions that take other functions as arguments or
# return functions

## closures

# closures are functions that capture the lexical scope in which they were
# defined, allowing them to access variables from that scope even when called
# outside of it


def multiplier(x):
    def mult(y):
        return x * y

    return mult


double = multiplier(2)
print(double(3))


## partial
def mult(y, x):
    return y * x


double = partial(mult, 2)
print(double(3))


def func(u, v, w, x):
    return u * 4 + v * 3 + w * 2 + x


p = partial(func, 10, 10, 10)
print(p(-30))


## decorators
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result

    return wrapper


@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")


## map-filer-reduce

arr = list(range(1_000))


def is_even(x):
    return x % 2 == 0


mapped = map(lambda x: x**2, arr)  # map can be applied to more than one iterable

# func must be a boolean function of one argument and only one iterable is allowed
filtered = filter(is_even, mapped)

# func must be a function of two arguments and only one iterable is allowed
initial = 0
reduced = reduce(
    lambda x, y: x + y, filtered, initial
)  # reduces the iterable to a single value


# map can be applied to more than one iterable
# number of args to lambda must match number of iterables
# basically [f(x, y) for (x, y) in zip(arr, arr2)]
arr2 = list(range(1_000, 2_000))
mapped2 = map(lambda x, y: x + y, arr, arr2)

# length of iterables does not have to match, but the result will be truncated
# to the length of the shortest iterable


def my_zip(X, Y):
    return list(map(lambda x, y: (x, y), X, Y))


# functional programming
# ----------------------

# functional programming is a programming paradigm that treats computation as
# the evaluation of mathematical functions and avoids changing state and
# mutable data. It emphasizes the use of higher-order functions, pure
# functions, and immutability.
