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
        for item in data:
            self._insert_at_end(item)


# FIXME
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
        if not self.head:
            print("Linked list is empty")
            return

        linked_list = []
        ptr = self.get_last_node()
        while ptr:
            linked_list.append(str(ptr.val))
            ptr = ptr.prev
        print(" <=> ".join(linked_list))

    def insert_at_beginning(self, val):
        if not self.head:
            node = Node(val, self.head)
            self.head = node
        else:
            node = Node(val, self.head)
            self.head.prev = node
            self.head = node
        self.size += 1

    def insert_at_end(self, val):
        ptr = self.head

        if not ptr:
            self.head = Node(val)
            self.size += 1
            return

        while ptr.next:
            ptr = ptr.next

        ptr.next = Node(val, next=None, prev=ptr)
        self.size += 1

    def insert(self, index, val):
        if index < 0 or index > len(self):
            raise IndexError()

        if index == 0:
            self.insert_at_beginning(val)
            return

        counter = 0
        ptr = self.head

        while ptr:
            if counter == (index - 1):
                node = Node(val, next=ptr.next, prev=ptr)
                if node.next:
                    node.next.prev = node
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
            self.size -= 1
            return

        counter = 0
        ptr = self.head

        while ptr:
            if counter == index:
                ptr.prev.next = ptr.next
                if ptr.next:
                    ptr.next.prev = ptr.prev
                self.size -= 1
                break
            ptr = ptr.next
            counter += 1

    def build(self, data):
        self.head = None
        for item in data:
            self.insert_at_end(item)

    def get_last_node(self):
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        return ptr
