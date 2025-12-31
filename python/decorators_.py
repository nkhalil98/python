from functools import wraps, update_wrapper
from time import time
from typing import Callable, List


# decorators
# ----------


# decorators are higher order functions that take a function as input and return
# a modified/enhanced version of that function without changing its code


## function decorators
def my_decorator(func: Callable) -> Callable:
    def wrapper():
        print("Doing some work before the function is called.")
        func()
        print("Doing some work after the function is called.")

    return wrapper


### using the decorator as a normal function
def say_hello():
    print("Hello!")


say_hello = my_decorator(say_hello)
say_hello()


### using the @ syntax for decorators
@my_decorator
def say_hello():
    print("Hello!")


## using functools.wraps to preserve function metadata

print(say_hello.__name__)  # prints "wrapper". The original function name is lost


def time_it(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Function {func.__name__} executed in {end - start} seconds")
        return result

    return wrapper


@time_it
def square(arr: List[int]) -> List[int]:
    return [x * x for x in arr]


arr = list(range(1_000_000))
arr_2 = square(arr)

print(square.__name__)  # prints "square". The original function name is preserved


## decorators with arguments (parameterized decorators/decorator factories)
def check_type(t: type) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, t):
                    raise TypeError(f"Positional argument {arg} is not of type {t}")
            for k, v in kwargs.items():
                if not isinstance(v, t):
                    raise TypeError(f"Keyword argument {k}={v} is not of type {t}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@check_type(int)
def add(a, b):
    return a + b


## class decorators
class TimerDecorator:
    def __init__(self, func: Callable):
        self.func = func
        update_wrapper(self, func)  # preserve function metadata

    def __call__(self, *args, **kwargs):
        start = time()
        result = self.func(*args, **kwargs)
        end = time()
        print(f"Function {self.func.__name__} executed in {end - start} seconds")
        return result


@TimerDecorator
def cube(arr: List[int]) -> List[int]:
    return [x**3 for x in arr]


arr_3 = cube(arr)

print(cube.__name__)  # prints "cube". The original function name is preserved


## stacking decorators
@time_it
@check_type(int)
def multiply(a, b):
    return a * b


result = multiply(5, 10)
