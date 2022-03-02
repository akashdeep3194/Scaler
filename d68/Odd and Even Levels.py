# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solveH(self, A):
        if A.left is None and A.right is None:
            return 0, A.val
        evenL = evenR = oddL = oddR = 0
        if A.left is not None:
            evenL, oddL = self.solveH(A.left)
        if A.right is not None:
            evenR, oddR = self.solveH(A.right)
        return oddL+oddR, A.val+evenL+evenR

    def solve(self, A):
        x = self.solveH(A)
        return x[1]-x[0]
