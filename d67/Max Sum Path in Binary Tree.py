# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxPathSum(self, A):
        return self.maxPathSumH(A)[0]

    def maxPathSumH(self, A):
        if A is None:
            return -10**9, 0
        ltms, lrms = self.maxPathSumH(A.left)
        rtms, rrms = self.maxPathSumH(A.right)
        ftms = lrms+rrms+A.val
        return max(ltms, rtms, ftms, A.val), max(lrms + A.val, rrms + A.val)


if __name__ == "__main__":
    s = Solution()
    n1 = TreeNode(-100)
    n2 = TreeNode(-200)
    n3 = TreeNode(-300)
    n4 = TreeNode(-400)

    n1.left = n2
    n2.left = n3
    n2.right = n4

    # n4 = TreeNode(32)
    # n5 = TreeNode(44)  # 6

    # n2.left = n4
    # n2.right = n5

    # n6 = TreeNode(17)  # 12
    # n7 = TreeNode(94)

    # n3.left = n6
    # n3.right = n7

    # n8 = TreeNode(29)
    # n9 = TreeNode(7)

    # n10 = TreeNode(35)
    # n11 = TreeNode(81)

    # n4.left = n8
    # n4.right = n9

    # n5.left = n10
    # n5.right = n11

    print(s.maxPathSum(n1))
