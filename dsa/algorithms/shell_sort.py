"""
Shell Sort
"""

from __future__ import annotations


def shell_sort(arr):
    if len(arr) <= 1:
        return

    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = anchor
        gap //= 2
