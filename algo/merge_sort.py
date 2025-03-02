# merge sort has a worst-case time complexity of O(nlog(n))
# merge sort has a space complexity of O(n)
# merge sort has a best-case time complexity of Ω(nlog(n))


def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge(left, right, arr)


def merge(a, b, arr):
    n = len(a)
    m = len(b)

    i = j = k = 0

    while i < n and j < m:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < n:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < m:
        arr[k] = b[j]
        j += 1
        k += 1
