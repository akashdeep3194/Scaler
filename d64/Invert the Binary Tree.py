# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        root = A
        if root is None:
            return root
        root.left, root.right = root.right, root.left,
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
