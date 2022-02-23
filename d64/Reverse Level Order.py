# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

from queue import Queue


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def solve(self, A):
        ans = []
        q = Queue()
        root = A
        q.put(root)
        q.put(None)
        while q.qsize() > 1:
            ele = q.get()
            if ele == None:
                q.put(None)
                continue
            if ele.right is not None:
                q.put(ele.right)
            if ele.left is not None:
                q.put(ele.left)
            ans.append(ele.val)
        return ans[::-1]
