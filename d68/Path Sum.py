# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer

    def hasPathSumH(self, A, B):
        if A.left is None and A.right is None:
            if B == A.val:
                return True
            else:
                return False
        lst = rst = False
        if A.left is not None:
            lst = self.hasPathSumH(A.left, B-A.val)
        if A.right is not None:
            rst = self.hasPathSumH(A.right, B-A.val)
        if lst or rst:
            return True
        else:
            return False

    def hasPathSum(self, A, B):
        if self.hasPathSumH(A, B):
            return 1
        else:
            return 0
