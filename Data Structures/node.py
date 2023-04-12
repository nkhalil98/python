class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
    def get_next_node(self):
        return self.next

    def set_next_node(self, node):
        self.next = node
        
    def get_val(self):
        return self.val
    
    def set_val(self, new_val):
        self.val = new_val
