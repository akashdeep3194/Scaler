# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorder(self, A, k, ctr=1, ans=None):
        if A is None:
            return ctr, ans
        ctr, ans = self.inorder(A.left, k, ctr, ans)
        if ctr == k:
            ans = A.val
        ctr += 1
        ctr, ans = self.inorder(A.right, k, ctr, ans)

        return ctr, ans

    def kthsmallest(self, A, B):
        ans = self.inorder(A, B)[1]
        return ans


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
    print(s.kthsmallest(n1, 3))
