# nodes are the fundamental building blocks of linked lists, stacks, queues, trees, and more

class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node
        
    def get_val(self):
        return self.val
    
    def set_val(self, new_val):
        self.val = new_val
