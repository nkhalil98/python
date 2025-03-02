from max_heap import MaxHeap
from min_heap import MinHeap


# heapsort implemented using max heap
def heapsort_max(arr):
    sorted_arr = []
    max_heap = MaxHeap()
    for el in arr:
        max_heap.add(el)
    while max_heap.count > 0:
        max_value = max_heap.retrieve_max()
        sorted_arr.insert(0, max_value)
    return sorted_arr


# heapsort implemented using min heap
def heapsort_min(arr):
    sorted_arr = []
    min_heap = MinHeap()
    for el in arr:
        min_heap.add(el)
    while min_heap.count > 0:
        min_value = min_heap.retrieve_min()
        sorted_arr.append(min_value)
    return sorted_arr
