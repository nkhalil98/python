# stack implementation using singly linked list

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

class Stack():
    def __init__(self, max_size=1000):
        self.top_item = None
        self.size = 0
        self.max_size = max_size
  
    def push(self, val):
        if self.has_space():
            item = Node(val, self.top_item)
            self.top_item = item
            self.size += 1
            return
        else:
            print("Stack is full!")
            return

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_val()
        else:
            print("Stack is empty!")
            return

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_val()
        else:
            print("Stack is empty!")

    def has_space(self):
        return self.size < self.max_size

    def is_empty(self):
        return self.size == 0
