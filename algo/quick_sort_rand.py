from random import randrange


def quicksort(arr, start, end):
    if start >= end:
        return

    pivot_idx = randrange(start, end + 1)
    pivot_element = arr[pivot_idx]
    arr[end], arr[pivot_idx] = arr[pivot_idx], arr[end]

    less_than_pivot = start

    for i in range(start, end):
        if arr[i] < pivot_element:
            arr[i], arr[less_than_pivot] = arr[less_than_pivot], arr[i]
            less_than_pivot += 1

    arr[end], arr[less_than_pivot] = arr[less_than_pivot], arr[end]

    quicksort(arr, start, less_than_pivot - 1)
    quicksort(arr, less_than_pivot + 1, end)
