class Node():
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, val):
        if not self.head:
            node = Node(val, self.head)
            self.head = node
        else:
            node = Node(val, self.head)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, val):
        node = Node(val)
        ptr = self.head

        if not ptr:
            self.head = node
            return

        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(val, None, ptr)

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
                node = Node(val, ptr.next, ptr)
                if node.next:
                    node.next.prev = node
                ptr.next = node
                break
            ptr = ptr.next
            counter += 1

    def remove(self, index):
        if index < 0 or index >= self.length():
            raise IndexError()
        
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        counter = 0
        ptr = self.head

        while ptr:
            if counter == index:
                ptr.prev.next = ptr.next
                if ptr.next:
                    ptr.next.prev = ptr.prev
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

    def get_last_node(self):
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        return ptr
    
    def print(self):
        linked_list = []
        ptr = self.head
        while ptr:
            linked_list.append(ptr.val)
            ptr = ptr.next
        print(linked_list)

    def print_backwards(self):
        linked_list = []
        ptr = self.get_last_node()
        while ptr:
            linked_list.append(ptr.val)
            ptr = ptr.prev
        print(linked_list)