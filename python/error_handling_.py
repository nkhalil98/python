import random


# python errors are of two types: syntax errors and runtime errors
# Some common built-in errors are: SyntaxError, NameError, TypeError,
# IndexError, IndentationError, KeyError, ValueError, ZeroDivisionError,
# FileNotFoundError, RecursionError, AttributeError, ImportError,
# ModuleNotFoundError, TimeoutError

numerator = 1
denominator = random.choice([0, 2, "a"])

# exception handling
# ------------------

## bare except (not recommended. don't use bare except)
try:
    print(numerator / denominator)
except:  # noqa
    print("An error occurred:")

## proper error handling (catch specific exceptions)
try:
    print(numerator / denominator)
except ZeroDivisionError:
    print("Cannot divide by zero")

## catch the exception object
try:
    print(numerator / denominator)
except ZeroDivisionError as e:
    print(e)

## catch multiple exceptions in a single except block
try:
    print(numerator / denominator)
except (ZeroDivisionError, TypeError):
    print("Cannot divide by zero or wrong type")

## multiple except blocks (better)
try:
    print(numerator / denominator)
except ZeroDivisionError:
    print("Cannot divide by zero")
except TypeError:
    print("Wrong type")

## fail silently (not recommended)
try:
    print(numerator / denominator)
except ZeroDivisionError:
    pass

## finally block (generally used for cleanup code)
try:
    print(numerator / denominator)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always run")

## else block
try:
    print(numerator / denominator)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:  # better than writing code in the try block in case the added code raises an exception that is accidentally caught by the except block
    print("This will run if no exception is raised")
finally:
    print("This will always run")


## example
def check_password():
    pass


def login_user():
    pass


def cleanup():
    pass


try:
    check_password()
except ValueError:
    print("Wrong Password! Try again!")
else:
    login_user()
finally:
    cleanup()

# it's not required to use except, else, finally together. You can use any
# combination of them


# user-defined exceptions and raise
# ---------------------------------

# all exceptions inherit from the BaseException class
# all user-defined exceptions must inherit from the Exception class


class MyException(Exception):
    pass


class MyOtherException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"MyOtherException: {self.message}"


try:
    print(numerator / denominator)
except ZeroDivisionError:
    raise MyException("This is my exception")
except TypeError:
    raise MyOtherException("This is my other exception")


# assertions
# ----------


def add_one(x):
    return x + 1


assert add_one(1) == 2
