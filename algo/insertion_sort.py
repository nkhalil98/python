"""
Insertion Sort
"""

from __future__ import annotations


def insertion_sort(arr):  # O(n^2)
    n = len(arr)
    if n <= 1:
        return

    for i in range(1, n):  # O(n)
        anchor = arr[i]
        j = i - 1  # pointer
        while j >= 0 and anchor < arr[j]:  # O(n)
            arr[j + 1] = arr[j]  # shift elements to the right
            j -= 1
        arr[j + 1] = anchor  # insert
