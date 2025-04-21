"""
Linear Search
"""

from __future__ import annotations


def linear_search(arr, e):  # O(n)
    for i in range(len(arr)):
        if arr[i] == e:
            return i

    return -1
