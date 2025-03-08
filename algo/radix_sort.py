"""
Radix Sort
    - LSD Radix Sort
"""

from __future__ import annotations


# least-significant-digit (LSD) implementation of radix sort
def radix_sort(arr):  # O(nk) where k is the number of digits in the largest number
    if not arr:
        return

    max_value = max(arr)
    max_exponent = len(str(max_value))
    to_sort = arr[:]

    for exponent in range(max_exponent):
        position = exponent + 1
        index = -position

        buckets = [[] for _ in range(10)]

        for num in to_sort:
            num_str = str(num)
            try:
                digit = num_str[index]
            except IndexError:
                digit = 0
            digit = int(digit)
            buckets[digit].append(num)

        to_sort = []

        for numeral in buckets:
            to_sort.extend(numeral)

    return to_sort
