# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer

    def solve(self, A, B, C):
        ans = self.solveH(A, B, C)
        return ans

    def solveH(self, A, B, C):
        if A is None:
            return 0
        cr = cl = 0
        if A.val <= C:
            cr = self.solveH(A.right, B, C)
        if A.val >= B:
            cl = self.solveH(A.left, B, C)
        if A.val <= C and A.val >= B:
            return cl + cr + 1
        else:
            return cl + cr
