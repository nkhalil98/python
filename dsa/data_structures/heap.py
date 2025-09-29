"""
Heap
    - Min Heap
    - Max Heap
"""

from __future__ import annotations


class MinHeap:
    def __init__(self):
        self.arr = [None]
        self.count = 0

    def __len__(self):
        return self.count

    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

    def add(self, element):
        self.arr.append(element)
        self.count += 1
        self.heapify_up()

    def heapify_up(self):
        idx = self.count
        while self.parent_idx(idx) > 0:
            if self.arr[self.parent_idx(idx)] > self.arr[idx]:
                self.arr[self.parent_idx(idx)], self.arr[idx] = (
                    self.arr[idx],
                    self.arr[self.parent_idx(idx)],
                )
            idx = self.parent_idx(idx)

    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            smaller_child_idx = self.get_smaller_child_idx(idx)
            if self.arr[idx] > self.arr[smaller_child_idx]:
                self.arr[smaller_child_idx], self.arr[idx] = (
                    self.arr[idx],
                    self.arr[smaller_child_idx],
                )
            idx = smaller_child_idx

    def retrieve_min(self):
        if self.count == 0:
            return None
        min_value = self.arr[1]
        self.arr[1] = self.arr[self.count]
        self.arr.pop()
        self.count -= 1
        self.heapify_down()
        return min_value

    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            return self.left_child_idx(idx)
        else:
            left_child = self.arr[self.left_child_idx(idx)]
            right_child = self.arr[self.right_child_idx(idx)]
            if left_child < right_child:
                return self.left_child_idx(idx)
            else:
                return self.right_child_idx(idx)


class MaxHeap:
    def __init__(self):
        self.arr = [None]
        self.count = 0

    def __len__(self):
        return self.count

    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

    def add(self, element):
        self.arr.append(element)
        self.count += 1
        self.heapify_up()

    def heapify_up(self):
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.arr[idx]
            parent = self.arr[self.parent_idx(idx)]
            if parent < child:
                self.arr[idx] = parent
                self.arr[self.parent_idx(idx)] = child
            idx = self.parent_idx(idx)

    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            larger_child_idx = self.get_larger_child_idx(idx)
            child = self.arr[larger_child_idx]
            parent = self.arr[idx]
            if parent < child:
                self.arr[idx] = child
                self.arr[larger_child_idx] = parent
            idx = larger_child_idx

    def retrieve_max(self):
        if self.count == 0:
            return None
        max_value = self.arr[1]
        self.arr[1] = self.arr[self.count]
        self.arr.pop()
        self.count -= 1
        self.heapify_down()
        return max_value

    def get_larger_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            return self.left_child_idx(idx)
        else:
            left_child = self.arr[self.left_child_idx(idx)]
            right_child = self.arr[self.right_child_idx(idx)]
            if left_child > right_child:
                return self.left_child_idx(idx)
            else:
                return self.right_child_idx(idx)
