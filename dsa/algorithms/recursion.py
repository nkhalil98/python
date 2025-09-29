from functools import wraps, lru_cache
from typing import Any, List


def non_negative(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int) or arg < 0:
                raise ValueError(f"Expected non-negative integer, got {arg}")
        for k, v in kwargs.items():
            if not isinstance(v, int) or v < 0:
                raise ValueError(f"Expected non-negative integer for {k}, got {v}")
        return func(*args, **kwargs)

    return wrapper


@non_negative
def sum_(n: int) -> int:
    if n == 0:
        return 0

    return n + sum_(n - 1)


@non_negative
def prod(n: int) -> int:
    if n == 0:
        return 0

    if n == 1:
        return 1

    return n * prod(n - 1)


@non_negative
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


@non_negative
def geometric_sum(n: int) -> float:
    if n == 0:
        return 1.0

    return 1 / (2**n) + geometric_sum(n - 1)


@non_negative
def harmonic_sum(n: int) -> float:
    if n == 0:
        return 0.0

    return 1 / n + harmonic_sum(n - 1)


@non_negative
def digit_sum(n: int) -> int:
    if n == 0:
        return 0

    return n % 10 + digit_sum(n // 10)


@non_negative
@lru_cache(maxsize=None)
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


@non_negative
def add(a: int, b: int) -> int:
    if b == 0:
        return a
    return add(a + 1, b - 1)


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
def gcd(a: int, b: int) -> int:
    a, b = max(a, b), min(a, b)

    if b == 0:
        return a

    return gcd(b, a % b)


def arr_sum(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    return nums[0] + arr_sum(nums[1:])


def arr_prod(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    return 0 if nums[0] == 0 else nums[0] * arr_prod(nums[1:])


def arr_find(arr: List[Any], e: Any) -> bool:
    if len(arr) == 0:
        return False

    if len(arr) == 1:
        return arr[0] == e

    return arr[0] == e or arr_find(arr[1:], e)


def arr_palindrome(arr: List[Any]) -> bool:
    if len(arr) == 0 or len(arr) == 1:
        return True

    return arr[0] == arr[-1] and arr_palindrome(arr[1:-1])


def flatten(arr: List[Any]) -> List[Any]:
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

    first = nums[0]
    without_first = power_set(nums[1:])
    with_first = [[first] + rest for rest in without_first]

    return with_first + without_first
