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
        if A is None:
            return 0, 0
        ansl, hl = self.solveH(A.left)
        ansr, hr = self.solveH(A.right)
        return max(ansl, ansr, hl+hr), max(hl, hr)+1

    def solve(self, A):
        return self.solveH(A)[0]
