"""
Heap Sort
"""

from data_structures.heap import MaxHeap, MinHeap


def heap_sort(arr, method="max"):
    methods = {"max": heapsort_max, "min": heapsort_min}

    sort_method = methods.get(method, heapsort_max)
    return sort_method(arr)


def heapsort_max(arr):
    sorted_arr = []
    max_heap = MaxHeap()
    for e in arr:
        max_heap.add(e)
    while len(max_heap) > 0:
        max_value = max_heap.retrieve_max()
        sorted_arr.insert(0, max_value)
    return sorted_arr


def heapsort_min(arr):
    sorted_arr = []
    min_heap = MinHeap()
    for e in arr:
        min_heap.add(e)
    while len(min_heap) > 0:
        min_value = min_heap.retrieve_min()
        sorted_arr.append(min_value)
    return sorted_arr
