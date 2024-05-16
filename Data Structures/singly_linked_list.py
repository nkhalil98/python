# linked lists are more memory efficient than built-in python arrays (no pre-allocation of memory)
# inserting/deleting elements at the beginning of a linked list is O(1)
# inserting/deleting elements at the end of a linked list is O(n)
# indexing in linked lists is O(n)

class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList():
    def __init__(self):
        self.head = None
        
    def get_head_node(self):
        return self.head

    def insert_at_beginning(self, val):
        node = Node(val, self.head)
        self.head = node

    def insert_at_end(self, val):
        node = Node(val)
        ptr = self.head

        if not ptr:
            self.head = node
            return

        while ptr.next:
            ptr = ptr.next
        ptr.next = node

    def insert(self, index, val):
        if index < 0 or index > self.length():
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
                break
            ptr = ptr.next
            counter += 1

    def remove(self, index):
        if index < 0 or index >= self.length():
            raise IndexError()
        
        if index == 0:
            self.head = self.head.next
            return

        counter = 0
        ptr = self.head

        while ptr:
            if counter == (index - 1):
                ptr.next = ptr.next.next
                break
            ptr = ptr.next
            counter += 1
    
    def build_linked_list(self, L):
        self.head = None
        for e in L:
            self.insert_at_end(e)
    
    def length(self):
        counter = 0
        ptr = self.head
        while ptr:
            counter += 1
            ptr = ptr.next
        return counter
    
    def print(self):
        linked_list = []
        ptr = self.head
        while ptr:
            linked_list.append(ptr.val)
            ptr = ptr.next
        print(linked_list)
