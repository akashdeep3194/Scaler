# Definition for a  binary tree node
import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


sys.setrecursionlimit(10**6)


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        arr = []
        ans = []
        root = A
        visited = dict()
        arr.append(root)
        while len(arr) > 0:
            x = arr.pop()
            if (x.left is None and x.right is None) or x in visited:
                ans.append(x.val)
                continue
            visited[x] = 1
            if x.right is not None:
                arr.append(x.right)
            arr.append(x)
            if x.left is not None:
                arr.append(x.left)

        return ans


if __name__ == "__main__":

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.right = n6
    s = Solution()
    ans = s.inorderTraversal(n1)
    print(ans)
