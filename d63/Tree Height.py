from sys import setrecursionlimit
setrecursionlimit(10**6)
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        if A is None:
            return 0
        sal = self.solve(A.left)
        sar = self.solve(A.right)

        return max(sal, sar)+1
