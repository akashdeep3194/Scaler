# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer

    def isSymmetricH(self, A, B):
        check_a_r_b_l = check_a_l_b_r = False
        if A.val == B.val:
            if (A.right is None and B.left is None):
                check_a_r_b_l = True
            if (A.left is None and B.right is None):
                check_a_l_b_r = True
            if (A.right is not None and B.left is not None):
                check_a_r_b_l = self.isSymmetricH(A.right, B.left)
            if (A.left is not None and B.right is not None):
                check_a_l_b_r = self.isSymmetricH(A.left, B.right)
            return check_a_l_b_r and check_a_r_b_l
        else:
            return False

    def isSymmetric(self, A):
        if A.left is not None and A.right is not None:
            if self.isSymmetricH(A.left, A.right):
                return 1
            else:
                return 0
        elif A.left is None and A.right is None:
            return 1
        else:
            return 0


if __name__ == "__main__":
    s = Solution()
    n1 = TreeNode(2)
    n2 = TreeNode(3)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(5)
    n7 = TreeNode(4)
    n8 = TreeNode(10)
    n9 = TreeNode(10)

    n1.left = n2
    n1.right = n3
    n2.left = n5
    n3.right = n6
    n5.right = n8
    n6.left = n9

    print(s.isSymmetric(n1))
