from queue import Queue
# Definition for a  binary tree node


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        ans = []
        arr = []
        q = Queue()
        q.put(A)
        q.put(None)
        while q.qsize() > 1:
            ele = q.get()

            if ele == None:
                ans.append(arr)
                arr = []
                q.put(None)
                continue

            if ele.left is not None:
                q.put(ele.left)
            if ele.right is not None:
                q.put(ele.right)

            arr.append(ele.val)
        ans.append(arr)
        return ans


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    n2 = TreeNode(4)
    n3 = TreeNode(5)
    root.left = n2
    root.right = n3

    print(s.levelOrder(root))
