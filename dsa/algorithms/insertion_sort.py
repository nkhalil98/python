"""
Insertion Sort
"""

from __future__ import annotations


def insertion_sort(arr):
    n = len(arr)
    if n <= 1:
        return

    for i in range(1, n):
        anchor = arr[i]
        j = i - 1
        while j >= 0 and anchor < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = anchor
