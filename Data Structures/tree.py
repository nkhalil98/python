# trees are nonlinear data structures that store hierarchical data in nodes
# the main node is called the root node
# nodes have parent and children nodes
# nodes that don't have children are called leafs

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.children = []

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def remove_child(self, child):
        self.children.remove(child)

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        
        print(prefix + self.data)
        
        if self.children:
            for child in self.children:
                child.print_tree()