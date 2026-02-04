from contextlib import contextmanager

# context managers
# ----------------

# context managers are used to manage resources
# context managers are invoked using the with statement


# using with statement to open a file
with open("example.txt") as f:
    f.read()


## user-defined context managers

# context managers implement the __enter__ and __exit__ protocols

### class-based context manager


class MyContextManager:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")


with MyContextManager() as cm:
    print("Inside context")


## function-based context manager


@contextmanager
def my_context_manager():
    print("Entering context")
    yield
    print("Exiting context")


with my_context_manager():
    print("Inside context")
