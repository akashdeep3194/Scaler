# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer

    def pre(self, A, ss):
        if A is None:
            return None
        ss.add(A.val)
        self.pre(A.left, ss)
        self.pre(A.right, ss)

    def common(self, A, ss, sm, z=10**9+7,):
        if A is None:
            return None
        if A.val in ss:
            sm[0] = (sm[0] + A.val) % z
        self.common(A.left, ss, sm=sm)
        self.common(A.right, ss, sm=sm)

    def solve(self, A, B):
        ss = set()
        sm = [0]
        self.pre(A, ss)
        self.common(B, ss, sm)
        return sm[0]
