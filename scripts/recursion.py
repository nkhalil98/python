from functools import wraps, lru_cache
from typing import Any, List


def non_negative(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int) or arg < 0:
                raise ValueError("All arguments must be non-negative integers")
        return func(*args)

    return wrapper


@non_negative
def total(n: int) -> int:
    if n == 0:
        return 0

    return n + total(n - 1)


@non_negative
def mult(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0

    if b == 1:
        return a

    return a + mult(a, b - 1)


@non_negative
def pow(n: int, p: int) -> int:
    if p == 0:
        return 1

    if p == 1:
        return n

    return n * pow(n, p - 1)


@non_negative
def factorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1

    return n * factorial(n - 1)


@non_negative
@lru_cache(maxsize=None)
def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def sum_(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    return nums[0] + sum_(nums[1:])


def prod(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    return nums[0] * prod(nums[1:])


def find(arr: List, e: Any) -> bool:
    if len(arr) == 0:
        return False

    if len(arr) == 1:
        return arr[0] == e

    return arr[0] == e or find(arr[1:], e)


def flatten(arr: List) -> List:
    result = []
    for e in arr:
        if isinstance(e, list):
            flat = flatten(e)
            result += flat
        else:
            result.append(e)
    return result


def power_set(nums: List[int]) -> List[List[int]]:
    if len(nums) == 0:
        return [[]]

    power_set_without_first = power_set(nums[1:])
    with_first = [[nums[0]] + rest for rest in power_set_without_first]

    return with_first + power_set_without_first
