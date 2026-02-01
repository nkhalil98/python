import logging
import traceback
import pdb


# comments
# TODO
# FIXME
# XXX


# debugging with print
def divide(a, b):
    print(f"Dividing {a} by {b}")  # debug print
    return a / b


result = divide(10, 2)
print(f"Result: {result}")

# uncomment the line below to see division by zero error
# result = divide(10, 0)


# logging
logging.basicConfig(level=logging.DEBUG)


def safe_divide(a, b):
    logging.debug(f"Dividing {a} by {b}")
    try:
        result = a / b
        logging.debug(f"Result: {result}")
        return result
    except ZeroDivisionError:
        logging.warning("Attempted to divide by zero. Coercing to 0", exc_info=True)
        return 0
    except TypeError:
        logging.error("Invalid types for division", exc_info=True)
        return None


# the traceback
def faulty_function():
    return 1 / 0  # this will raise a ZeroDivisionError


try:
    faulty_function()
except ZeroDivisionError:
    print("Caught an exception:")
    traceback.print_exc()


# using pdb
def buggy_function():
    x = 10
    y = 0
    result = x / y  # this will raise a ZeroDivisionError
    return result


# uncomment the line below to invoke the debugger on exception
# pdb.run("buggy_function()")


# setting breakpoints
arr1 = list(range(1_000))
arr2 = list(range(1_000, 2_000))

arr2[500] = 0  # introduce a zero to cause division by zero error
arr2[700] = "a"  # introduce a non-numeric value to cause TypeError

div = []
for i in range(1_000):
    a = arr1[i]
    b = arr2[i]
    try:
        div.append(a / b)
    except:  # noqa
        breakpoint()  # set a breakpoint here
