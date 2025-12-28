"""
N-ary Tree
"""

from __future__ import annotations

from typing import List


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parent: TreeNode | None = None
        self.children: List[TreeNode] = []

    def add_child(self, child: TreeNode):
        self.children.append(child)
        child.parent = self

    def remove_child(self, child: TreeNode):
        self.children.remove(child)
        child.parent = None

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return len(self.children) == 0

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def max_depth(self):
        if self.is_leaf():
            return 1
        return 1 + max(child.max_depth() for child in self.children)

    def __str__(self):
        lines = []

        def traverse(node: TreeNode):
            indent = " " * node.get_level() * 2
            prefix = indent + "└── " if node.parent else ""
            result = f"{prefix}{node.value}".rjust(3)
            lines.append(result)
            for child in node.children:
                traverse(child)

        traverse(self)
        return "\n".join(lines)
