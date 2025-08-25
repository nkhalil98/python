# printing
# --------
print("Hello, World!")


# comments
# --------
# this is a comment


# variables
# ---------
a = 1  # variable assignment with the assignment operator (=)
a = "hello"  # python is dynamically typed (variable type can change)
a, b = 1, 2  # multiple assignment
a, b = b, a  # swap values of two variables
CONST = 3  # python does not have true constants (by convention, constants are written in uppercase)
# python keywords cannot be used as variable names


# user input
# ----------
prompt = "Enter your name: "
name = input(prompt)
print("Hello, " + name)


# built-in data types
# -------------------

## native data types
a = 1  # int (integer)
b = 2.3  # float (floating-point number)
x = True  # bool (Boolean - True or False)
n = None  # NoneType

## sequence data types
my_str = "hello"  # str (string - immutable sequence of characters)
my_list = [1, 2, 3, "foo", [4, 5]]  # list (dynamic array of elements)
my_tuple = (1, 2, 3)  # tuple (immutable sequence of elements)

## sequence operations
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

### length
n = len(nums)  # length of the sequence

### indexing (0-based)
first = nums[0]  # first element
last = nums[-1]  # can use negative indexing to access elements from the end

### slicing [start:end:step]
middle = nums[4:7]  # start index is inclusive, end index is exclusive
every_other = nums[::2]  # slicing with step
reversed = nums[::-1]  # reverse the list (negative step)

### concatenation and repetition
more_nums = nums + [11, 12, 13]  # concatenate two lists
repeated = nums * 2  # repeat the list

## mapping data types: dict (dictionary/hashmap/hash table/associative array)
my_dict = {"name": "Nabil", "age": 26}  # key-value pairs
name = my_dict["name"]  # access a value using a key
my_dict["city"] = "Boston"  # add a new key-value pair

## set data types
my_set = {1, 2, 3}  # set (unordered collection of unique elements)

## type casting
to_str = str(1)  # int to str
to_int = int("1")  # str to int

## type checking
# everything in python is an object and each object has a type
a = 1
print(type(a))  # int
print(isinstance(a, int))  # True


# operators
# ---------

## arithmetic
a + b  # addition
a - b  # subtraction
a * b  # multiplication
a / b  # division
a // b  # integer/floor/C division
a % b  # modulo
a**b  # exponentiation

## comparison/relational
a > b  # greater than
a < b  # less than
a == b  # equal to
a != b  # not equal to
a >= b  # greater than or equal to
a <= b  # less than or equal to

## logical
a and b  # and
a or b  #  or
not a  # not

## assignment
a = 1
a += 1  # increment
a -= 1  # decrement

## membership
a in b  # True if a contains b

## identity
a is b  # True if both variables reference the same object in memory


# control flow
# -----------

## conditional statements

### if statement
if a > 0:
    print("a is positive")

### if-else statement
names = ["Alice", "Bob", "Charlie"]
if "Alice" in names:
    print("Alice is in the list")
else:
    print("Alice is not in the list")

### if-elif-else statement
a = 80
if a > 0:
    print("a is positive")
elif a == 0:
    print("a is zero")
else:
    print("a is negative")
# python does not require an else block at the end of an if-elif chain

### short-circuiting and multiple if statements
a = 200

if a > 100:
    print("Greater than 100")
elif a > 50:
    print("Greater than 50")
elif a > 0:
    print("Positive")
# prints only "Greater than 100" and skips the rest

if a > 100:
    print("Greater than 100")
if a > 50:
    print("Greater than 50")
if a > 0:
    print("Positive")
# prints all three statements because each if is evaluated independently


## loops

### for loops
L = [1, 2, 3]

### index-based iteration
for i in range(len(L)):  # for i in range(n)
    print(L[i])

### element-based iteration
for element in L:  # for element in iterable
    print(element)

### while loops

#### with a counter
counter = 0
while counter < 10:
    print(counter)
    counter += 1

#### with updating an iterable
L = [1, 2, 3]
while L:
    print(L.pop())

#### with a flag
active = True
while active:
    print("Hello")
    active = False

#### continue and break statements
for i in range(10):
    if i % 2 == 1:  # skip odd numbers
        continue
    print(i)

for i in range(10):
    if i == 5:  # stop the loop when i is 5
        break
    print(i)

### list comprehensions
nums = [1, 2, 3, 4, 5]
squares = [x**2 for x in nums]


# functions
# ---------


## function definition
def greet():  # no arguments (parameters)
    """
    This is a docstring. It is used to document the function.

    This function greets the user.
    """
    print("Hello")  # no return value (returns None)


greet()  # function call


## function arguments
def add(x, y):  # positional arguments only
    return x + y


def add2(x, y, z=0):  # keyword argument with a default value
    return x + y + z


x1 = add2(1, 2)  # z = 0
x2 = add2(1, 2, 3)  # z = 3


## functions can return multiple values (technically returns a tuple)
def add_sub(x, y):
    return x + y, x - y


a, b = add_sub(2, 1)


## functions can modify mutable arguments (lists, dictionaries, sets) in-place
def square(L):
    for i in range(len(L)):
        L[i] = L[i] ** 2


L1 = [1, 2, 3]
L2 = [4, 5, 6]
square(L1)  # L1 = [1, 4, 9]
square(L2[:])  # pass a copy to avoid modifying the original list - L2 = [4, 5, 6]


## arbitrary number of arguments
def add_nums(*args):  # args is a tuple
    return sum(args)


sum1 = add_nums(1, 2, 3, 4, 5)
sum2 = add_nums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


## arbitrary number of keyword arguments
def parse_id(**kwargs):  # kwargs is a dictionary
    for k, v in kwargs.items():
        print(k, v)


parse_id(id=0, name="Nabil", age=26)


# file I/O
# --------

## reading

### reading the entire file
f = open("filename.txt")
content = f.read()
lines = content.splitlines()
for line in lines:
    print(line)
f.close()  # close the file to free up resources


### using with statement (context manager)
with open("filename.txt") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        print(line)

##  writing

### writing to a file
f = open("filename2.txt", "w")
f.write("Hi")
f.close()

### using with statement
with open("filename2.txt", "w") as f:
    f.write("Hello")

### appending to a file
with open("filename2.txt", "a") as f:
    f.write(" World\n")


# error handling
# --------------
# Some common errors are: SyntaxError, NameError, TypeError, IndexError,
# IndentationError, KeyError, ValueError, ZeroDivisionError, FileNotFoundError

## exceptions
try:
    print(1 / 0)
except:  # noqa
    print("An error occurred:")
# don't use bare except

try:
    print(1 / 0)
except ZeroDivisionError:  # catch specific exceptions
    print("Cannot divide by zero")

try:
    print(1 / 0)
except ZeroDivisionError:
    pass  # silently ignore the error

try:
    print(1 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always run")

try:
    print(1 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("This will run if no exception is raised")
finally:
    print("This will always run")

try:
    raise Exception("This is an exception")
except Exception as e:  # catch the exception object
    print(e)


# classes
# -------


## class definition
class Person:
    # initializer
    def __init__(self, name, age):  # dunder/magic method
        self.name = name  # instance variable/attribute
        self.age = age
        self.id = None  # default value

    # instance method
    def greet(self):
        print("Hello, my name is", self.name)

    def speak(self):
        print("I am speaking")

    # getter method
    def get_id(self):
        return self.id

    # setter method
    def set_id(self, id):
        assert isinstance(id, int), "ID must be an integer"
        self.id = id


p = Person("Nabil", 26)  # object instantiation
p.greet()  # method call
print("My age is: ", p.age)  # access instance attribute

p.id = 1  # direct access to instance attribute
p.set_id(2)  # using setter method


## inheritance
class Student(Person):  # Student is a subclass of Person superclass
    def __init__(self, name, age, school):
        super().__init__(name, age)  # explicitly call the superclass initializer
        self.school = school

    def study(self):
        print("I am studying")

    # method overriding
    def speak(self):
        print("I am a student")


s = Student("Nabil", 26, "MIT")
s.greet()  # method from superclass
s.speak()  # overridden method
s.study()  # method from subclass

print(issubclass(Student, Person))  # True
print(isinstance(s, Student))  # True
print(isinstance(s, Person))  # True
