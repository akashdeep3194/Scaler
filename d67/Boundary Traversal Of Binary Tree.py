# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def get_leaves(self, A, leaf):
        if A is None:
            return
        if A.left is None and A.right is None:
            leaf.append(A.val)
        self.get_leaves(A.left, leaf)
        self.get_leaves(A.right, leaf)

    def solve(self, A):
        if A.left is None and A.right is None:
            return [A.val]
        root = A
        left = []
        right = []
        leaf = []
        while root is not None:
            if root.left is None and root.right is None:
                break
            left.append(root.val)
            root = root.left

        root = A.right
        while root is not None:
            if root.left is None and root.right is None:
                break
            right.append(root.val)
            root = root.right

        self.get_leaves(A, leaf)
        left.extend(leaf)
        left.extend(right[::-1])
        return left
