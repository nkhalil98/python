class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

    def add(self, element):
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        idx = self.count
        while self.parent_idx(idx) > 0:
            if self.heap_list[self.parent_idx(idx)] > self.heap_list[idx]:
                self.heap_list[self.parent_idx(idx)], self.heap_list[idx] = self.heap_list[idx], self.heap_list[self.parent_idx(idx)]
            idx = self.parent_idx(idx)   
            
    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            smaller_child_idx = self.get_smaller_child_idx(idx)
            if self.heap_list[idx] > self.heap_list[smaller_child_idx]:
                self.heap_list[smaller_child_idx], self.heap_list[idx] = self.heap_list[idx], self.heap_list[smaller_child_idx]
            idx = smaller_child_idx

    def retrieve_min(self):
        if self.count == 0:
            print("Heap is empty!")
            return None
        min_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        self.heapify_down()
        return min_value

    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child < right_child:
                return self.left_child_idx(idx)
            else:
                return self.right_child_idx(idx)