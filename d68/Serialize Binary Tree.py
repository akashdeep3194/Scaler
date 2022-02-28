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

    def solve(self, A):
        ans = []
        q = Queue()
        q.put(A)
        # q.put(None)
        while q.qsize() > 0:
            ele = q.get()
            if ele == -1:
                ans.append(-1)
                continue
            else:
                ans.append(ele.val)
            if ele.left is not None:
                q.put(ele.left)
            else:
                q.put(-1)
            if ele.right is not None:
                q.put(ele.right)
            else:
                q.put(-1)
        return ans


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    n2 = TreeNode(4)
    n3 = TreeNode(5)
    root.left = n2
    root.right = n3

    print(s.solve(root))
