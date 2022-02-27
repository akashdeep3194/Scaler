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
    def solve(self, A, B, C):
        ans = self.solveH(A, B, C)
        return ans[0]

    def solveH(self, A, B, C):
        if A is None:
            return -1, 2

        ls, ll = self.solveH(A.left, B, C)
        rs, rr = self.solveH(A.right, B, C)
        if ll == 0:
            return ls, 0
        elif rr == 0:
            return rs, 0

        if ls != -1 and rs != -1:
            return ls+rs, 0

        elif ls != -1:
            if(A.val == B or A.val == C):
                return ls, 0
            else:
                return ls + 1, 1
        elif rs != -1:
            if (A.val == B or A.val == C):
                return rs, 0
            else:
                return rs + 1, 1
        else:
            if (A.val == B and A.val == C):
                return 0, 2
            elif (A.val == B or A.val == C):
                return 1, 1

            return -1, 2


if __name__ == "__main__":
    s = Solution()
    n1 = TreeNode(15)
    n2 = TreeNode(23)
    n3 = TreeNode(16)
    n1.left = n2
    n1.right = n3

    n4 = TreeNode(38)
    n5 = TreeNode(8)  # 6

    n2.left = n4
    n2.right = n5

    n6 = TreeNode(18)  # 12
    n7 = TreeNode(32)

    n3.left = n6
    n3.right = n7

    n8 = TreeNode(40)
    n4.right = n8
    print(s.solve(n1, 18, 40))
