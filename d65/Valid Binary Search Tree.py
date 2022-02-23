# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        ans = self.isValidBSTH(A)[2]
        if ans:
            return 1
        else:
            return 0

    def isValidBSTH(self, A):
        if A.left is None and A.right is None:
            return A.val, A.val, True
        if A.left is not None:
            maxl, minl, lst = self.isValidBSTH(A.left)
        if A.right is not None:
            maxr, minr, rst = self.isValidBSTH(A.right)

        if A.left is not None and A.right is not None:
            if lst and rst:
                if A.val > maxl and A.val < minr:
                    return max(A.val, maxl, maxr), min(A.val, minl, minr), True
                else:
                    return -1, -1, False
            else:
                return -1, -1, False

        elif A.left is not None:
            if lst and A.val > maxl:
                return max(A.val, maxl), min(A.val, minl), True
            else:
                return -1, -1, False

        elif A.right is not None:
            if rst and A.val < minr:
                return max(A.val, maxr), min(A.val, minr), True
            else:
                return -1, -1, False
