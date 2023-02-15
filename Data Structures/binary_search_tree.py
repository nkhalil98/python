# a binary tree is a tree where every node has at most 2 children
# a strict/proper binary tree is a binary tree where each node can have either 0 or 2 children
# a complete binary tree is a binary tree where all levels possibly the last are completely filled and all nodes are as left as possible
# a perfect binary tree is a binary tree where all levels are filled
# a binary tree can have a maximum of 2^i nodes at level i
# maximum number of nodes in a binary tree of height h is 2^(h+1) - 1
# min height of a binary tree with n nodes is in a perfect binary tree which is log2(n)
# max height of a binary tree with n nodes is in a sparse binary tree which is n-1
# a balanced binary tree is a binary tree where the difference between the height of the left sub-tree and the right sub-tree for every node is not more than k (usually 1)
# in binary search tree any node is smaller than a node to its right and larger than a node to its left
# binary search trees cannot contain duplicate elements
# searching for an element in a BST is O(log(n))
# a BST can be traversed using in-order traversal (left sub-tree -> root -> right sub-tree), pre-order traversal (root -> left sub-tree -> right sub-tree), or post-order traversal (left sub-tree -> right sub-tree -> root)

class BinarySearchTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def add_child(self, val):
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


    def search(self, val):
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

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.val)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.val)

        return elements

    def pre_order_traversal(self):
        elements = [self.val]

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def delete(self, val):
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

    def delete2(self, val):
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

    def find_max(self):
        if self.right is None:
            return self.val
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.val
        return self.left.find_min()
    
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.val + left_sum + right_sum