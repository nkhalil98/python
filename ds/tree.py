"""
Tree
"""

from __future__ import annotations


class TreeNode:
    def __init__(self, val):  # O(1)
        self.val = val
        self.parent = None
        self.children = []

    def get_level(self):  # O(n)
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def add_child(self, child: TreeNode):  # O(1)
        child.parent = self
        self.children.append(child)

    def remove_child(self, child):  # O(n)
        self.children.remove(child)

    def print_tree(self):  # O(n)
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""

        print(prefix + str(self.val))

        if self.children:
            for child in self.children:
                child.print_tree()
