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
    def zigzagLevelOrder(self, A):
        dir = -1
        ans = []
        arr = []
        q = Queue()
        root = A
        q.put(root)
        q.put(None)
        while q.qsize() > 1:
            ele = q.get()
            if ele == None:
                if dir == 1:
                    ans.append(arr[::-1])
                else:
                    ans.append(arr)
                dir *= -1
                q.put(None)
                arr = []
                continue
            if ele.left is not None:
                q.put(ele.left)
            if ele.right is not None:
                q.put(ele.right)
            arr.append(ele.val)
        if dir == 1:
            ans.append(arr[::-1])
        else:
            ans.append(arr)
        return ans
