# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        if self.isBalancedH(A)[1]:
            return 1
        else:
            return 0

    def isBalancedH(self, A):
        root = A
        if root is None:
            return 0, True
        dlt, islb = self.isBalancedH(root.left)
        drt, isrb = self.isBalancedH(root.right)
        if isrb and islb:
            if abs(dlt-drt) <= 1:
                return max(dlt, drt)+1, True
            else:
                return -1, False
        else:
            return -1, False
