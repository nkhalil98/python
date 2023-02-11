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