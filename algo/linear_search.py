# Linear search is a brute force searching algorithm that sequentially checks whether a given value is an element of a specified arary by scanning the elements of a list one-by-one until it finds the target value
# Linear search runs in O(n) time


def linear_search(arr, e):
    n = len(arr)
    for i in range(n):
        if arr[i] == e:
            return i
    return -1
