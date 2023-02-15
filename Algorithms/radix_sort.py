# radix sort has a worst-case time complexity of O(nk)
# radix sort has a space complexity of O(n+k)
# radix sort has a best-case time complexity of Ω(nk)


# implementing a least-significant-digit implementation of radix sort
def radix_sort(arr):
	max_value = max(arr)
	max_exponent = len(str(max_value))
	to_sort = arr[:]

	for exponent in range(max_exponent):
		position = exponent + 1
		index = -position

		buckets = [[] for i in range(10)]

		for num in to_sort:
			num_str = str(num)
			try:
				digit = num_str[index]
			except IndexError:
				digit = 0
			digit = int(digit)
			buckets[digit].append(num)
			
		to_sort = []

		for numeral in buckets:
			to_sort.extend(numeral)

	return to_sort