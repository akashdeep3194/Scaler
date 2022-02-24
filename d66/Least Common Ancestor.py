# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        ans = self.lcaH(A, B, C)
        if ans[1] == 2:
            return ans[0]
        else:
            return -1

    def lcaH(self, A, B, C):
        if A is None:
            return -1, 0

        lca_l = self.lcaH(A.left, B, C)
        lca_r = self.lcaH(A.right, B, C)
        if lca_l[1] == 2:
            return lca_l[0], lca_l[1]
        if lca_r[1] == 2:
            return lca_r[0], lca_r[1]

        lca_l = lca_l[0]
        lca_r = lca_r[0]

        if lca_l != -1 and lca_r != -1:
            return A.val, 2

        elif lca_l != -1:
            if lca_l == B and A.val == C:
                return A.val, 2
            if lca_l == C and A.val == B:
                return A.val, 2
            return lca_l, 1

        elif lca_r != -1:
            if lca_r == B and A.val == C:
                return A.val, 2
            if lca_r == C and A.val == B:
                return A.val, 2
            return lca_r, 1
        elif A.val == B and A.val == C:
            return A.val, 2
        elif A.val == B or A.val == C:
            return A.val, 1
        return -1, 0


if __name__ == "__main__":
    s = Solution()
    n1 = TreeNode(10)
    n2 = TreeNode(4)
    n3 = TreeNode(20)
    n1.left = n2
    n1.right = n3

    n4 = TreeNode(0)
    n5 = TreeNode(6)  # 6

    n2.left = n4
    n2.right = n5

    n6 = TreeNode(12)  # 12
    n7 = TreeNode(25)

    n3.left = n6
    n3.right = n7

    n8 = TreeNode(11)
    n6.right = n8
    print(s.lca(n1, 4, 6))
