"""
Bubble Sort
"""

from __future__ import annotations


# optimized bubble sort: O(n) best-case time complexity
def bubble_sort(arr):  # O(n^2)
    n = len(arr)
    if n <= 1:
        return

    for i in range(n - 1):  # O(n)
        swapped = False
        for j in range(n - 1 - i):  # O(n)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
                swapped = True
        if not swapped:
            break


def bubble_sort_unoptimized(arr):  # O(n^2)
    n = len(arr)
    if n <= 1:
        return

    for _ in range(n):  # O(n)
        for j in range(n - 1):  # O(n)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
