"""
Merge Sort
"""

from __future__ import annotations


def merge_sort(arr):  # O(nlog(n))
    if len(arr) <= 1:  # base case
        return arr

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    left_sorted = merge_sort(left)  # O(n/2)
    right_sorted = merge_sort(right)  # O(n/2)

    return merge(left_sorted, right_sorted, arr)  # O(n)


def merge(a, b, arr):  # O(n)
    n = len(a)
    m = len(b)

    i = j = k = 0

    while i < n and j < m:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < n:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < m:
        arr[k] = b[j]
        j += 1
        k += 1

    return arr


# unoptimized merge implementation that uses an additional O(n) space instead of
# merging in place
def merge_unoptimized(left, right):  # O(n)
    merged = []

    while left and right:
        if left[0] < right[0]:
            merged.append(left[0])
            left.pop(0)
        else:
            merged.append(right[0])
            right.pop(0)

    if left:
        merged += left

    if right:
        merged += right

    return merged
