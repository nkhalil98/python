"""
Shell Sort
"""

from __future__ import annotations


def shell_sort(arr):  # O(n(log(n))^2)
    if len(arr) <= 1:
        return

    n = len(arr)
    gap = n // 2

    while gap > 0:  # O(log(n))
        for i in range(gap, n):  # O(n)
            anchor = arr[i]
            j = i
            while j >= gap and arr[j - gap] > anchor:  # O(log(n))
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = anchor
        gap //= 2
