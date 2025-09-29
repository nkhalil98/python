"""
Bubble Sort
"""

from __future__ import annotations


def bubble_sort(arr):
    n = len(arr)

    if n <= 1:
        return

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def bubble_sort_unoptimized(arr):
    n = len(arr)

    if n <= 1:
        return

    for _ in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
