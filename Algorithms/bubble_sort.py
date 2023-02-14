# bubble sort has a worst-case time complexity of O(n^2)
# bubble sort has a space complexity of O(1)
# bubble sort has a best-case time complexity of O(n)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break