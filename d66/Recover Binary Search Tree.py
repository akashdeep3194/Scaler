# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorder(self, A,  f=0, prev=-10**9, min_val=10**9, ans=[10**-9, 10**-9]):
        if A is None:
            return f, prev, min_val
        f, prev, min_val = self.inorder(A.left,  f, prev, min_val, ans)
        if f == 0:
            if A.val >= prev:
                prev = A.val
            else:
                ans[0] = prev
                min_val = A.val
                ans[1] = min_val

                prev = A.val
                f = 1
        else:
            min_val = min(min_val, A.val)
            ans[1] = min_val

        f, prev, min_val = self.inorder(A.right,  f, prev, min_val, ans)

        return f, prev, min_val

    def recoverTree(self, A):
        ans = [10**-9, 10**-9]
        self.inorder(A,  ans=ans)
        return ans[::-1]


if __name__ == "__main__":
    s = Solution()
    n1 = TreeNode(10)
    n2 = TreeNode(4)
    n3 = TreeNode(20)
    n1.left = n2
    n1.right = n3

    n4 = TreeNode(0)
    n5 = TreeNode(12)  # 6

    n2.left = n4
    n2.right = n5

    n6 = TreeNode(6)  # 12
    n7 = TreeNode(25)

    n3.left = n6
    n3.right = n7

    n8 = TreeNode(11)
    n6.right = n8
    print(s.recoverTree(n1))
    #             10
    #     4               20
    # 0       12       6      25
    #                     11
