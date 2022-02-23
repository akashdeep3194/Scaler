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
        if self.solveH(A)[1] == True:
            return 1
        else:
            return 0

    def solveH(self, A):
        root = A
        if root is None:
            return (0, True)
        if root.left is None and root.right is None:
            return (root.val, True)
        sal, sbl = self.solveH(root.left)
        sar, sbr = self.solveH(root.right)
        if sbl and sbr:
            if sar + sal == root.val:
                return (sal+sar+root.val, True)
            else:
                return (0, False)
        else:
            return (0, False)
