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

    def __str__(self):  # O(n)
        lines = []

        def traverse(node):
            indent = " " * node.get_level() * 2
            prefix = indent + "└── " if node.parent else ""
            result = f"{prefix}{node.val}".rjust(3)
            lines.append(result)
            for child in node.children:
                traverse(child)

        traverse(self)
        return "\n".join(lines)
