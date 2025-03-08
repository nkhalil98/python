"""
Binary Search
    - Iterative Binary Search
    - Recursive Binary Search
"""

from __future__ import annotations


def binary_search(arr, e, method="iterative"):  # O(log(n))
    if not arr:
        return -1

    methods = {
        "iterative": binary_search_iter,
        "recursive": binary_search_recur,
    }

    search_method = methods.get(method, binary_search_iter)
    return search_method(arr, e)


# binary search iterative implementation
def binary_search_iter(arr, e):  # O(log(n))
    if not arr:
        return -1

    left = 0  # left pointer
    right = len(arr) - 1  # right pointer

    while left <= right:
        mid = (left + right) // 2
        mid_number = arr[mid]

        if mid_number == e:
            return mid

        if mid_number < e:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# binary search recursive implementation
def binary_search_recur(arr, e, left, right):  # O(log(n))
    if not arr:
        return -1

    if right < left:
        return -1

    mid = (left + right) // 2
    mid_number = arr[mid]

    if mid_number == e:
        return mid

    if mid_number < e:
        return binary_search_recur(arr, e, mid + 1, right)
    else:
        return binary_search_recur(arr, e, left, mid - 1)
