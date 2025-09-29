"""
Merge Sort
"""

from __future__ import annotations


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted, arr)


def merge(a, b, arr):
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


def merge_unoptimized(left, right):
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
