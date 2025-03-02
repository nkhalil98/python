# shell sort is an optimization over insertion sort as insertion sort requires many swaps and comparisons if heavy elements are located towards the end of sorted array being built
# shell sort will initially sort subarrays of elements that are equal distance (gap) apart
# we keep on reducing the gap until it is 1. then this happens, shell sort becomes insertion sort and will carry with less comparisons and swaps
# shell sort has a worst-case time complexity of O(n(log(n))^2)
# shell sort has a space complexity of O(1)
# shell sort has a best-case time complexity of Ω(nlog(n))


def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = anchor
        gap //= 2
