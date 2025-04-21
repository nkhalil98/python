"""
Binary Search
    - Iterative Binary Search
    - Recursive Binary Search
"""

from __future__ import annotations


# binary search iterative implementation
def binary_search(arr, e):  # O(log(n))
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == e:
            return mid
        elif arr[mid] < e:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# binary search recursive implementation
def binary_search_recursive(arr, e, left=None, right=None):  # O(log(n))
    if left is None:
        left = 0

    if right is None:
        right = len(arr) - 1

    if right < left:
        return -1

    mid = (left + right) // 2

    if arr[mid] == e:
        return mid
    elif arr[mid] < e:
        left = mid + 1
    else:
        right = mid - 1

    return binary_search_recursive(arr, e, left, right)
