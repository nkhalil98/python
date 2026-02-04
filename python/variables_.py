import keyword


# expressions vs statements
# -------------------------

1 + 2  # expression (evaluates to a value)
a = 1  # statement (does something)
# python does not require semicolons to terminate statements

# variables and types
# -------------------

# variables are names (identifiers) that reference objects (values in memory)

## variable assignment
# assignment creates a new reference to an object in memory
# "=" is the assignment operator and not an equality operator like in
# mathematics. Assignment is not the same as equality.

a = 1  # variable assignment (lhs: variable name -> assignment operator (=) -> rhs: expression or value)
a = 2  # variables can be reassigned to new values
a = a + 1  # a variable can also be assigned to an expression involving itself
CONST = 3  # python does not have constants (use uppercase for naming constants by convention)
CONST = 4  # reassigning constant is allowed but not recommended

## dynamic typing
# variables can be reassigned to objects of different types and python infers
# types at runtime
a = 1
a = "hello"


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

# python loads built-in names (like int, str, list, dict, etc.) into the global
# namespace at startup using the builtins module (see sys.modules['builtins'])
# or print(dir(__builtins__))

# python built-in functions (like int, str, print, dir, etc.) can be shadowed by
# variable names but it is not recommended practice
int = "shadowed"  # shadows built-in int()
print(int)  # prints "shadowed"
del int  # delete shadowing variable to restore built-in int()
print(int("123"))  # prints 123  # noqa

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

# all python objects have types that can be checked at runtime using type() and
# isinstance()

a = 1
print(type(a))  # int
print(isinstance(a, int))  # True  # noqa

## type casting
a = int("123")  # string to int  # noqa
is_truthy = bool(1)  # can even cast to bool
# empty values (0, "", [], {}, None, etc.) are falsy; everything else is truthy
