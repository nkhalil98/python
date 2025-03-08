"""
Selection Sort
"""

from __future__ import annotations


def selection_sort(arr):  # O(n^2)
    n = len(arr)
    if n <= 1:
        return

    for i in range(n - 1):  # O(n)
        min_index = find_min(arr, i)  # O(n)
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]  # swap


def find_min(arr, start):  # O(n)
    n = len(arr)
    min_index = start
    for i in range(start + 1, n):
        if arr[i] < arr[min_index]:
            min_index = i
    return min_index
