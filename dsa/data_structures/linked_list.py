"""
Linked List
    - Singly Linked List
    - Doubly Linked List
"""

from __future__ import annotations


class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


# TODO: implement reverse, remove_all, has_cycle, sort
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        ptr = self.head
        while ptr:
            yield ptr.val
            ptr = ptr.next

    def __str__(self):
        if not self.head:
            return "Empty Linked List"

        linked_list = []
        ptr = self.head
        while ptr:
            linked_list.append(str(ptr.val))
            ptr = ptr.next
        return " => ".join(linked_list)

    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError()

        counter = 0
        ptr = self.head

        while ptr:
            if counter == index:
                return ptr.val
            ptr = ptr.next
            counter += 1

    def __setitem__(self, index, value):
        if index < 0 or index >= len(self):
            raise IndexError()

        counter = 0
        ptr = self.head

        while ptr:
            if counter == index:
                ptr.val = value
                return
            ptr = ptr.next
            counter += 1

    def __deleteitem__(self, index):
        self.pop(index)

    def _insert_at_beginning(self, val):
        node = Node(val, self.head)
        self.head = node
        self.size += 1

    def _insert_at_end(self, val):
        node = Node(val)
        ptr = self.head

        if not ptr:
            self.head = node
            self.size += 1
            return

        while ptr.next:
            ptr = ptr.next

        ptr.next = node
        self.size += 1

    append = _insert_at_end

    def insert(self, index, val):
        if index < 0 or index > len(self):
            raise IndexError()

        if index == 0:
            self._insert_at_beginning(val)
            return

        if index == len(self):
            self._insert_at_end(val)
            return

        counter = 0
        ptr = self.head

        while ptr:
            if counter == (index - 1):
                node = Node(val, ptr.next)
                ptr.next = node
                self.size += 1
                break
            ptr = ptr.next
            counter += 1

    def pop(self, index=None):
        if index is None:
            index = self.size - 1

        if index < 0 or index >= len(self):
            raise IndexError()

        if index == 0:
            val = self.head.val
            self.head = self.head.next
            self.size -= 1
            return val

        counter = 0
        ptr = self.head

        while ptr:
            if counter == (index - 1):
                val = ptr.next.val
                ptr.next = ptr.next.next
                self.size -= 1
                return val
            ptr = ptr.next
            counter += 1

    def remove(self, val):
        if self.head is None:
            return

        if self.head.val == val:
            self.head = self.head.next
            self.size -= 1
            return

        ptr = self.head
        while ptr.next:
            if ptr.next.val == val:
                ptr.next = ptr.next.next
                self.size -= 1
                return
            ptr = ptr.next

    def build(self, data):
        self.head = None
        self.size = 0

        for item in data:
            self._insert_at_end(item)

    def to_list(self):
        result = []
        ptr = self.head

        while ptr:
            result.append(ptr.val)
            ptr = ptr.next

        return result

    def find(self, val):
        ptr = self.head
        index = 0

        while ptr:
            if ptr.val == val:
                return index
            ptr = ptr.next
            index += 1

        return -1

    def swap(self, i, j):
        if i < 0 or i >= len(self) or j < 0 or j >= len(self):
            raise IndexError()

        if i == j:
            return

        if i > j:
            i, j = j, i

        prev_i = None
        curr_i = self.head
        for _ in range(i):
            prev_i = curr_i
            curr_i = curr_i.next

        prev_j = None
        curr_j = self.head
        for _ in range(j):
            prev_j = curr_j
            curr_j = curr_j.next

        if prev_i:
            prev_i.next = curr_j
        else:
            self.head = curr_j

        if prev_j:
            prev_j.next = curr_i
        else:
            self.head = curr_i

        temp = curr_i.next
        curr_i.next = curr_j.next
        curr_j.next = temp

    def nth_last_node(self, n):
        current = None
        leader = self.head
        count = 0

        while leader:
            leader = leader.next
            count += 1
            if count >= n:
                if current is None:
                    current = self.head
                else:
                    current = current.next

        return current

    def nth_last_node_2(self, n):
        current, leader = self.head, self.head
        for _ in range(n):
            if leader is None:
                return None
            leader = leader.next

        while leader:
            current = current.next
            leader = leader.next

        return current

    def find_middle_node(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.head
        while node:
            yield node.val
            node = node.next

    def __str__(self):
        if not self.head:
            return "Empty Doubly Linked List"

        linked_list = []
        ptr = self.head
        while ptr:
            linked_list.append(str(ptr.val))
            ptr = ptr.next
        return " <=> ".join(linked_list)

    def print_backwards(self):
        if not self.tail:
            print("Empty Doubly Linked List")
            return

        linked_list = []
        ptr = self.tail
        while ptr:
            linked_list.append(str(ptr.val))
            ptr = ptr.prev
        print(" <=> ".join(linked_list))

    def insert_at_beginning(self, val):
        if not self.head and not self.tail:
            node = Node(val)
            self.head = node
            self.tail = node
        else:
            node = Node(val, self.head, None)
            self.head.prev = node
            self.head = node
        self.size += 1

    def insert_at_end(self, val):
        if not self.head and not self.tail:
            node = Node(val)
            self.head = node
            self.tail = node
        else:
            node = Node(val, None, self.tail)
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert(self, index, val):
        if index < 0 or index > len(self):
            raise IndexError()

        if index == 0:
            self.insert_at_beginning(val)
            return

        if index == len(self):
            self.insert_at_end(val)
            return

        counter = 0
        ptr = self.head

        while ptr:
            if counter == (index - 1):
                node = Node(val, next=ptr.next, prev=ptr)
                ptr.next.prev = node
                ptr.next = node
                self.size += 1
                break
            ptr = ptr.next
            counter += 1

    def remove(self, index):
        if index < 0 or index >= len(self):
            raise IndexError()

        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self.size -= 1
            return

        if index == len(self) - 1:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            self.size -= 1
            return

        counter = 0
        ptr = self.head

        while ptr:
            if counter == index:
                ptr.prev.next = ptr.next
                ptr.next.prev = ptr.prev
                self.size -= 1
                break
            ptr = ptr.next
            counter += 1

    def build(self, data):
        self.head = None
        self.tail = None
        self.size = 0
        for item in data:
            self.insert_at_end(item)
