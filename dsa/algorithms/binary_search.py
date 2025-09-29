"""
Binary Search
"""

from __future__ import annotations


def binary_search(arr, e):
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


def binary_search_recursive(arr, e, left=None, right=None):
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


def binary_search_slice(arr, e):
    if not arr:
        return False

    mid = len(arr) // 2

    if arr[mid] == e:
        return True
    elif arr[mid] < e:
        return binary_search_slice(arr[mid + 1 :], e)
    else:
        return binary_search_slice(arr[:mid], e)
