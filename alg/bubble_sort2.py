def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort_unoptimized(arr):
    n = len(arr)
    for el in arr:
        for i in range(n-1):
          if arr[i] > arr[i+1]:
              swap(arr, i, i+1)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
