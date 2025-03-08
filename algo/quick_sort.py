"""
Quick Sort
"""

from __future__ import annotations

from random import randrange


def quick_sort(arr, method="hoare"):
    if not arr:
        return arr

    methods = {
        "hoare": hoare_quick_sort,
        "lomuto": lomuto_quick_sort,
        "random": random_quicksort,
    }

    sort_method = methods.get(method, hoare_quick_sort)
    sort_method(arr, 0, len(arr) - 1)
    return arr


# quick sort implementation using hoare partition scheme
def hoare_quick_sort(arr, start, end):  # O(nlog(n))
    if start < end:
        p_index = hpartition(arr, start, end)  # O(n)
        hoare_quick_sort(arr, start, p_index - 1)  # O(log(n))
        hoare_quick_sort(arr, p_index + 1, end)  # O(log(n))


def hpartition(arr, start, end):  # O(n)
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:
        while start <= end and arr[start] <= pivot:
            start += 1

        while start <= end and arr[end] > pivot:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]

    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

    return end


# quick sort implementation using lomuto partition scheme
def lomuto_quick_sort(arr, start, end):  # O(nlog(n))
    if start >= end:
        return
    p_index = lpartition(arr, start, end)  # O(n)
    lomuto_quick_sort(arr, start, p_index - 1)  # O(log(n))
    lomuto_quick_sort(arr, p_index + 1, end)  # O(log(n))


def lpartition(arr, start, end):  # O(n)
    pivot = arr[end]
    p_index = start

    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[p_index] = arr[p_index], arr[i]
            p_index += 1

    arr[p_index], arr[end] = arr[end], arr[p_index]

    return p_index


# quick sort implementation using random pivot
def random_quicksort(arr, start, end):  # O(nlog(n))
    if start >= end:
        return

    pivot_idx = randrange(start, end + 1)
    pivot_element = arr[pivot_idx]
    arr[end], arr[pivot_idx] = arr[pivot_idx], arr[end]

    less_than_pivot = start

    for i in range(start, end):  # O(n)
        if arr[i] < pivot_element:
            arr[i], arr[less_than_pivot] = arr[less_than_pivot], arr[i]
            less_than_pivot += 1

    arr[end], arr[less_than_pivot] = arr[less_than_pivot], arr[end]

    random_quicksort(arr, start, less_than_pivot - 1)  # O(log(n))
    random_quicksort(arr, less_than_pivot + 1, end)  # O(log(n))
