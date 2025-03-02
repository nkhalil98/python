# selection sort has a worst-case time complexity of O(n^2)
# selection sort has a space complexity of O(1)
# selection sort has a best-case time complexity of Ω(n^2)


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(min_index + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
