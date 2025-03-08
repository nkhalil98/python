"""
Linear Search
"""

from __future__ import annotations


def linear_search(arr, e):  # O(n)
    if not arr:
        return -1

    n = len(arr)

    for i in range(n):
        if arr[i] == e:
            return i
    return -1
