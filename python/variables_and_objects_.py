import dis
import inspect
import keyword
import sys


# TODO: object introspection

# expressions vs statements
# -------------------------

1 + 2  # expression (evaluates to a value)
a = 1  # statement (does something)
# python does not require semicolons to terminate statements

# variables and types
# -------------------

## variable assignment
# assignment creates a new reference to an object in memory
a = 1  # variable assignment (lhs: variable name -> assignment operator (=) -> rhs: expression or value)
CONST = 3  # python does not have constants (use uppercase for naming constants by convention)
CONST = 4  # reassigning constant is allowed but not recommended

## dynamic typing
a = "hello"  # python is dynamically typed
# python infers types at runtime and variables can change type at runtime

# statically typed languages (like C) require variable declaration with its type
# (like int a;) before assignment
# variable value can change at runtime but its type cannot

## type hinting
# type hints were introduced in PEP 484 (Python 3.5+)
b: int = 1  # optional type hinting
s: str  # python does not have type declarations (referencing s before assignment raises NameError)
s = 10  # type hinting is not enforced at runtime

## strong typing
s + b  # python is strongly typed meaning types are enforced at runtime

# python does not implicitly convert types (like JavaScript); for example,
# adding incompatible types (a + b) raises TypeError


## duck typing
# "if it looks like a duck and quacks like a duck, it's a duck"
def quack_and_fly(duck):
    duck.quack()
    duck.fly()


# any object with quack() and fly() methods can be passed to quack_and_fly()
class Duck:
    def quack(self):
        print("Quack!")

    def fly(self):
        print("Flap flap!")


class Person:
    def quack(self):
        print("I'm quacking like a duck!")

    def fly(self):
        print("I'm flapping my arms!")


duck = Duck()
person = Person()
quack_and_fly(duck)  # works
quack_and_fly(person)  # works
# no need for explicit interfaces or type checks

## more on variable assignment
f, g, h = 1, 2, 3  # multiple assignment (f = 1, g = 2, h = 3)
c = d = e = 1  # chained assignment (c = 1, d = 1, e = 1)
a, b = b, a  # swapping values of a and b (a = 1, b = "hello")

### assignment vs aliasing
a = (1, 2, 3)  # assignment of immutable object (tuple)
aa = a  # assignment of immutable object (tuple); aa references same object as a
a = (4, 5, 6)  # re-assignment creates a new object in memory
print(a is aa)  # False; a references new object, aa references old object

b = [1, 2, 3]
bb = b  # assignment of mutable object (list); bb references same object as b
b.append(4)  # modifying mutable object
print(b is bb)  # True; b and bb reference same modified object

## variable naming rules

# variable names can only contain alphanumeric characters and underscores
# variable names cannot be reserved keywords (if, else, while, etc.) and cannot
# start with a number

## soft keywords
# python has soft keywords (like match, case) that are only keywords in specific
# contexts
print(keyword.kwlist)

## shadowing built-ins
# python built-in functions (like int, str, print, dir, etc.) can be shadowed by
# variable names but it is not recommended practice
int = "shadowed"  # shadows built-in int()
print(int)  # prints "shadowed"
del int  # delete shadowing variable to restore built-in int()

# variable naming conventions were introduced in PEP 8

## conclusion

# python variables are really two things:

# 1. a name (identifier) stored in a namespace (scope)
print(globals())  # global namespace
print(locals())  # local namespace
print(vars())  # current namespace

# 2. an object (value in memory)
print(id(a))  # memory address of object referenced by a

# the name references the object in memory

## type checking
a = 1
print(type(a))  # int
print(isinstance(a, int))  # True

## type casting
a = int("123")  # string to int
is_truthy = bool(1)  # can even cast to bool
# empty values (0, "", [], {}, None, etc.) are falsy; everything else is truthy


# python built-in data types: numeric - boolean - NoneType - sequence - mapping
# - set - binary - ellipsis - Exceptions
# -----------------------------------------------------------------------------

## object
obj = object()  # every object in python derives from the (featureless) object class
print(type(obj))  # <class 'object'>

## numeric
a = 1  # int
b = 1.0  # float
c1 = 1 + 2j  # complex number
c2 = complex(1, 2)  # complex number

## boolean
bb = True  # bool

## NoneType
nn = None  # NoneType

## sequence
s = "hello"  # str
arr = [1, 2, 3]  # list
tup = (1, 2, 3)  # tuple

## range
rng = range(10)

## mapping
data = {"key": "value"}  # dict

## set
ss = {1, 2, 3}  # set
fs = frozenset([1, 2, 3])  # frozenset


# function
def foo():  # function object
    pass


# type
class MyClass:  # type object
    pass


t = type(MyClass)  # type object
type(t)  # type object


## exceptions
e = BaseException()  # BaseException

## binary
h = b"hello"  # bytes
i = bytearray(b"hello")  # bytearray: mutable bytes
j = memoryview(b"hello")  # memoryview: memory view of bytes

## ellipsis
e = Ellipsis  # Ellipsis object
e2 = ...  # Ellipsis literal


# zip
z = zip([1, 2, 3], ["a", "b", "c"])  # zip object

# enumerate
en = enumerate(["a", "b", "c"])  # enumerate object

# generator
gen = (x * x for x in range(5))  # generator object

# map and filter
m = map(lambda x: x * x, range(5))  # map object
f = filter(lambda x: x % 2 == 0, range(10))  # filter object


# coroutine
async def coro():
    pass


coro_obj = coro()  # coroutine objectc


# objects
# -------

# python data model: everything in python is an object and every object has a
# type



