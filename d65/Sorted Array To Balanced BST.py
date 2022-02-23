# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        return self.sortedArrayToBSTH(A, 0, len(A)-1)

    def sortedArrayToBSTH(self, A, si, ei):
        if si > ei:
            return None
        mid = (si + ei)//2
        root = TreeNode(A[mid])
        lst = self.sortedArrayToBSTH(A, si, mid-1)
        rst = self.sortedArrayToBSTH(A, mid+1, ei)
        root.left = lst
        root.right = rst

        return root
