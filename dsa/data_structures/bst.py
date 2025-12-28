"""
Binary Tree
    - Binary Search Tree (BST)
"""

from __future__ import annotations


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __contains__(self, value):
        if self.value == value:
            return True

        found_in_left = self.left and value in self.left
        found_in_right = self.right and value in self.right

        return found_in_left or found_in_right

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.value)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = [self.value]

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.value)

        return elements


class BinarySearchTreeNode(BinaryTreeNode):
    def __init__(self, value):
        super().__init__(value)

    def __contains__(self, value):
        if self.value == value:
            return True

        if value < self.value:
            if self.left:
                return value in self.left
            else:
                return False

        if value > self.value:
            if self.right:
                return value in self.right
            else:
                return False

    def add_child(self, value):
        if value == self.value:
            return

        if value < self.value:
            if self.left:
                self.left.add_child(value)
            else:
                self.left = BinarySearchTreeNode(value)
        else:
            if self.right:
                self.right.add_child(value)
            else:
                self.right = BinarySearchTreeNode(value)

    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_value = self.right.find_min()
            self.value = min_value
            self.right = self.right.delete(min_value)

        return self

    def delete2(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            max_value = self.left.find_max()
            self.value = max_value
            self.left = self.left.delete(max_value)

        return self

    def find_max(self):
        if self.right is None:
            return self.value
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.value
        return self.left.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.value + left_sum + right_sum

    def height(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)

    def build(self, elements):
        self.value = elements[0]
        for element in elements[1:]:
            self.add_child(element)
        return self
