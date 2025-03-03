"""
Linked List
    - Singly Linked List
    - Doubly Linked List
"""

from __future__ import annotations


class Node:
    def __init__(self, val=None, next=None, prev=None):  # O(1)
        self.val = val
        self.next = next
        self.prev = prev


class SinglyLinkedList:
    def __init__(self):  # O(1)
        self.head = None
        self.size = 0

    def __len__(self):  # O(1)
        return self.size

    def __iter__(self):  # O(n)
        node = self.head
        while node:
            yield node.val
            node = node.next

    def insert_at_beginning(self, val):  # O(1)
        node = Node(val, self.head)
        self.head = node
        self.size += 1

    def insert_at_end(self, val):  # O(n)
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

    def insert(self, index, val):  # O(n)
        if index < 0 or index > len(self):
            raise IndexError()

        if index == 0:
            self.insert_at_beginning(val)
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

    def remove(self, index):  # O(n)
        if index < 0 or index >= len(self):
            raise IndexError()

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        counter = 0
        ptr = self.head

        while ptr:
            if counter == (index - 1):
                ptr.next = ptr.next.next
                self.size -= 1
                break
            ptr = ptr.next
            counter += 1

    def build(self, data):  # O(n)
        self.head = None
        for item in data:
            self.insert_at_end(item)

    def length(self):  # O(n)
        counter = 0
        ptr = self.head
        while ptr:
            counter += 1
            ptr = ptr.next
        return counter

    def print(self):  # O(n)
        if not self.head:
            print("Linked list is empty")
            return

        linked_list = []
        ptr = self.head
        while ptr:
            linked_list.append(str(ptr.val))
            ptr = ptr.next
        print(" --> ".join(linked_list))


class DoublyLinkedList:
    def __init__(self):  # O(1)
        self.head = None
        self.size = 0

    def __len__(self):  # O(1)
        return self.size

    def __iter__(self):  # O(n)
        node = self.head
        while node:
            yield node.val
            node = node.next

    def insert_at_beginning(self, val):  # O(1)
        if not self.head:
            node = Node(val, self.head)
            self.head = node
        else:
            node = Node(val, self.head)
            self.head.prev = node
            self.head = node
        self.size += 1

    def insert_at_end(self, val):  # O(n)
        ptr = self.head

        if not ptr:
            self.head = Node(val)
            self.size += 1
            return

        while ptr.next:
            ptr = ptr.next

        ptr.next = Node(val, next=None, prev=ptr)
        self.size += 1

    def insert(self, index, val):  # O(n)
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

    def remove(self, index):  # O(n)
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

    def build(self, data):  # O(n)
        self.head = None
        for item in data:
            self.insert_at_end(item)

    def length(self):  # O(n)
        counter = 0
        ptr = self.head
        while ptr:
            counter += 1
            ptr = ptr.next
        return counter

    def get_last_node(self):  # O(n)
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        return ptr

    def print(self):  # O(n)
        if not self.head:
            print("Linked list is empty")
            return

        linked_list = []
        ptr = self.head
        while ptr:
            linked_list.append(str(ptr.val))
            ptr = ptr.next
        print(" <--> ".join(linked_list))

    def print_backwards(self):  # O(n)
        if not self.head:
            print("Linked list is empty")
            return

        linked_list = []
        ptr = self.get_last_node()
        while ptr:
            linked_list.append(str(ptr.val))
            ptr = ptr.prev
        print(" <--> ".join(linked_list))
