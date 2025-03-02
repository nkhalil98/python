# insertion sort has a worst-case time complexity of O(n^2)
# insertion sort has a space complexity of O(1)
# insertion sort has a best-case time complexity of Ω(n)


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        anchor = arr[i]
        j = i - 1
        while j >= 0 and anchor < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = anchor
