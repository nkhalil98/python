# boolean values and boolean expressions
# --------------------------------------

## python has a built-in bool type with two values: True and False
true = True
false = False


## boolean expressions are expressions that evaluate to boolean values (True or False)
bool_expr1 = 5 > 3  # True
bool_expr2 = 2 + 2 == 5  # False

# relational, logical, membership, identity operators, and boolean functions are
# used to create boolean expressions

## relational/comparison operators
eq = 5 == 5  # True
neq = 5 != 3  # True
lt = 3 < 5  # True
lte = 5 <= 5  # True
gt = 10 > 5  # True
gte = 10 >= 10  # True


## logical operators (AND, OR, XOR, NOT)
and_op = (5 > 3) and (2 < 4)  # True
or_op = (5 > 3) or (2 > 4)  # True
not_op = not (5 > 3)  # False

### truth tables for logical operators:

# AND
# A     B     A and B
# True  True   True
# True  False  False
# False True   False
# False False  False

# OR
# A     B     A or B
# True  True   True
# True  False  True
# False True   True
# False False  False

# XOR
# A     B     A xor B
# True  True   False
# True  False  True
# False True   True
# False False  False

# NOT
# A     not A
# True  False
# False True


# logical operators have short-circuit evaluation meaning an AND operation
# will stop evaluating as soon as one operand is False, and an OR operation
# will stop evaluating as soon as one operand is True

# logical operator precedence: NOT > AND > OR

# python does not have a built-in xor operator but we can use the != or the
# bitwise ^ operator with boolean values to achieve the same effect
xor_op = (5 > 3) != (2 > 4)  # True
xor_op2 = (5 > 3) ^ (2 > 4)  # True

## membership operators
my_list = [1, 2, 3, 4, 5]
in_op = 3 in my_list  # True
not_in_op = 6 not in my_list  # True

## identity operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
is_op = a is b  # True
is_not_op = a is not c  # True


## boolean functions
# a boolean function is a function that returns a boolean value
def is_even(n):
    return n % 2 == 0


is_even_op = is_even(4)  # True
is_odd_op = not is_even(5)  # True

# conditional statements
# ----------------------

# if statements execute a block of code if a condition is true
# python uses indentation (over curly braces in other languages like C) to
# define code blocks
# indentation style: 4 spaces per indentation level

a = 5

## if statement
if a > 3:  # condition
    print("a is greater than 3")

## if-else statement
# only one of the blocks will be executed based on the condition
if a > 3:  # condition
    print("a is greater than 3")
else:  # else block
    print("a is not greater than 3")

## if-elif-else statement (chained conditionals)
# conditionals are short-circuited, meaning once a condition is met, the code
# block is executed and the rest of the conditions are skipped
a = 80
if a > 100:  # condition 1
    print("Greater than 100")
elif a > 50:  # condition 2
    print("Greater than 50")
elif a > 25:  # condition 3
    print("Greater than 25")
elif a > 0:  # condition 4
    print("Positive")
elif a == 0:  # condition 5
    print("Zero")
else:  # all other cases
    print("Negative")

## if-elif statement (without else)
# python does not require an else block at the end of the if-elif chain
if a > 10:  # condition 1
    print("a is greater than 10")
elif a > 5:  # condition 2
    print("a is greater than 5")
elif a > 0:  # condition 3
    print("a is greater than 0")


## multiple conditionals (independent if statements)
# sometimes we want to check multiple independent conditions without
# short-circuiting
if a > 100:  # if block 1
    print("Greater than 100")
if a > 50:  # if block 2
    print("Greater than 50")
if a > 0:  # if block 3
    print("Positive")


# nested conditionals
# -------------------

num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    if num == 0:
        print("Zero")
    else:
        print("Negative number")

## refactoring a nested conditional example
num = 15
if num > 0 and num % 2 == 0:
    print("Positive even number")
elif num > 0 and num % 2 != 0:
    print("Positive odd number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# truthy and falsy values
# -----------------------

# in conditional contexts, non-boolean values are evaluated as boolean values
if False:
    print("This will never be printed")

if not []:
    print("This will be printed because the list is empty")


# falsy values: None, False, 0, 0.0, and empty collections (e.g., "", [], {}, set())
# truthy values: all other values

# to check the boolean value of an object, use the built-in bool() function
bool_none = bool(None)  # False

# another way to check for truthy/falsy values is to use double negation
bool_empty_str = not not ""  # False
bool_non_empty_str = not not "Hello"  # True


# match-case statements (Python 3.10+)
# ------------------------------------

# match-case statements are similar to switch-case statements in other languages

status = 404
match status:
    case 400:
        print("Bad Request")
    case 401:
        print("Unauthorized")
    case 403:
        print("Forbidden")
    case 404:
        print("Not Found")
    case _:  # default case
        print("Something went wrong")


## more complex match-case example
num_str = "3"
match int(num_str):
    case 1 | 2 | 3:
        print("Low number")
    case 4 | 5 | 6:
        print("Medium number")
    case 7 | 8 | 9:
        print("High number")
    case _:  # default case
        print("Out of range")

## structural pattern matching
data = [10, 20, 30]
match data:
    case [x, y, _]:  # matches a list with at least three elements, ignoring the third
        print(f"First two elements are {x} and {y}")
    case {
        "name": name,
        "age": _,
    }:  # matches a dictionary with 'name' and 'age', ignoring age's value
        print(f"Person's name is {name}")

my_list = [1, 2, 3, 4, 5]
match my_list:
    case [
        first,
        second,
        *_,
    ]:  # matches a list with at least two elements, ignoring the rest
        print(f"First: {first}, Second: {second}")

## using guards in match-case
point = (3, 4)
match point:
    case (x, y) if x == y:
        print(f"Point is on the line y=x at ({x}, {y})")
    case (x, y) if x == -y:
        print(f"Point is on the line y=-x at ({x}, {y})")
    case (x, y):
        print(f"Point is at ({x}, {y})")


command = ["go", "north"]
match command:
    case ["go", direction] if direction in ["north", "south", "east", "west"]:
        print(f"Moving in direction: {direction}")
    case ["go", _]:
        print("Invalid direction")
    case _:
        print("Unknown command")


# ternary operator (conditional expression)
# -----------------------------------------
a = 10
b = 20
max_ = a if a > b else b  # similar to max_ = (a > b) ? a : b in other languages


# pass statement
# --------------

# pass is a null statement that does nothing, used as a placeholder

a = 5
b = 10

if a > b:
    pass  # placeholder for future code
else:
    print("a is not greater than b")
