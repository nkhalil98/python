"""
Binary Search Tree (BST)
"""

from __future__ import annotations


class BinarySearchTreeNode:
    def __init__(self, val):  # O(1)
        self.val = val
        self.left = None
        self.right = None

    def add_child(self, val):  # O(log n) average, O(n) worst
        if val == self.val:
            return

        if val < self.val:
            if self.left:
                self.left.add_child(val)
            else:
                self.left = BinarySearchTreeNode(val)
        else:
            if self.right:
                self.right.add_child(val)
            else:
                self.right = BinarySearchTreeNode(val)

    def search(self, val):  # O(log n) average, O(n) worst
        if self.val == val:
            return True

        if val < self.val:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.val:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):  # O(n)
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.val)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):  # O(n)
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.val)

        return elements

    def pre_order_traversal(self):  # O(n)
        elements = [self.val]

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def delete(self, val):  # O(log n) average, O(n) worst
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.val:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.val = min_val
            self.right = self.right.delete(min_val)

        return self

    def delete2(self, val):  # O(log n) average, O(n) worst
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

    def find_max(self):  # O(log n) average, O(n) worst
        if self.right is None:
            return self.val
        return self.right.find_max()

    def find_min(self):  # O(log n) average, O(n) worst
        if self.left is None:
            return self.val
        return self.left.find_min()

    def calculate_sum(self):  # O(n)
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.val + left_sum + right_sum
