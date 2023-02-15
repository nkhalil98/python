# bianry search is a searching algorithm that searches for an element in a sorted dataset in O(log(n)) time opposed to linear search that does it in O(n) time

def binary_search_iter(arr, number_to_find):
    left = 0
    right = len(arr) - 1
    mid = 0

    while left <= right:
        mid = (left + right) // 2
        mid_number = arr[mid]

        if mid_number == number_to_find:
            return mid

        if mid_number < number_to_find:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def binary_search_recur(arr, number_to_find, left, right):
    if right < left:
        return -1

    mid = (left + right) // 2
    mid_number = arr[mid]

    if mid >= len(arr) or mid < 0:
        return -1

    if mid_number == number_to_find:
        return mid

    if mid_number < number_to_find:
        left = mid + 1
    else:
        right = mid - 1

    return binary_search_recur(arr, number_to_find, left, right)