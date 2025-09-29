"""
Selection Sort
"""

from __future__ import annotations


def selection_sort(arr):
    n = len(arr)

    if n <= 1:
        return

    for i in range(n - 1):
        min_index = _find_min(arr, i)
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]  # swap


def selection_sort_unoptimized(arr):
    sorted_arr = []

    while arr:
        min_index = _find_min(arr, 0)
        sorted_arr.append(arr.pop(min_index))

    return sorted_arr


def _find_min(arr, start):
    n = len(arr)
    min_index = start

    for i in range(start + 1, n):
        if arr[i] < arr[min_index]:
            min_index = i

    return min_index
