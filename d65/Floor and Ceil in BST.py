# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : list of integers
    # @return a list of list of integers
    def floor_ceil(self, A, ele):
        floor = ceil = -1
        root = A
        while A is not None:
            if A.val == ele:
                return ele, ele
            elif A.val > ele:
                ceil = A.val
                A = A.left
            else:
                A = A.right

        A = root

        while A is not None:
            if A.val == ele:
                return ele, ele
            elif A.val < ele:
                floor = A.val
                A = A.right
            else:
                A = A.left

        return floor, ceil

    def solve(self, A, B):
        ans = []
        for ele in B:
            ans.append(list(self.floor_ceil(A, ele)))
        return ans
