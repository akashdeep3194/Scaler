# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorder(self, A, arr):
        if A is None:
            return
        self.inorder(A.left, arr)
        arr.append(A.val)
        self.inorder(A.right, arr)

    def recoverTree(self, A):
        arr = []
        ans = []
        f = 0
        self.inorder(A, arr)
        for i in range(len(arr)-1):
            ele = arr[i]
            if f == 1 and ele < arr[i-1]:
                ans.append(ele)
                return ans[::-1]
            if ele > arr[i+1]:
                ans.append(ele)
                f = 1
