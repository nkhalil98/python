# quick sort has a worst-case time complexity of O(n^2)
# quick sort has a space complexity of O(log(n))
# quick sort has a best-case time complexity of Ω(nlog(n))
# quick sort has a average-case time complexity of Θ(nlog(n)

# implementation of quick sort in python using hoare partition scheme
def quick_sort(arr, start, end):
    if start < end:
        p_index = partition(arr, start, end)
        quick_sort(arr, start, p_index - 1)
        quick_sort(arr, p_index + 1, end)


def partition(arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1

        while arr[end] > pivot:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]

    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

    return end
