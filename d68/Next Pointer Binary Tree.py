# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root.left is None:
            return
        root.left.next = root.right
        root = root.left
        while root.left is not None:
            temp = root
            while temp is not None:
                temp.left.next = temp.right
                if temp.next is not None:
                    temp.right.next = temp.next.left
                else:
                    temp.right.next = None
                temp = temp.next
            root = root.left
