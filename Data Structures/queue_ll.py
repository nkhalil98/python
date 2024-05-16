# queue implementation using singly linked list

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def set_next_node(self, node):
        self.next = node
    
    def get_next_node(self):
        return self.next
        
    def get_val(self):
        return self.val

class Queue():
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0
    
    def enqueue(self, val):
        if self.has_space():
            item_to_add = Node(val)
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Queue is full!")
         
    def dequeue(self):
        if self.get_size() > 0:
            item_to_remove = self.head
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_val()
        else:
            print("Queue is empty!")
  
    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            return self.head.get_val()
  
    def get_size(self):
        return self.size
  
    def has_space(self):
        if self.max_size is None:
            return True
        return self.size < self.max_size
    
    def is_empty(self):
        return self.size == 0