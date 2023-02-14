def merge_sort(items):
    if len(items) <= 1:
        return items

    mid_index = len(items) // 2

    left = items[:mid_index]
    right = items[mid_index:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []

    while (left and right):
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if left:
        result += left

    if right:
        result += right

    return result