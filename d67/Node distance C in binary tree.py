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
    # @return a list of integers
    def path_to_node(self, A, B, ans=[]):
        if A is None:
            return None
        if A.val == B:
            ans.append(A)
            return ans
        lp = self.path_to_node(A.left, B, ans)
        rp = self.path_to_node(A.right, B, ans)
        if lp is not None or rp is not None:
            ans.append(A)
            return ans
        else:
            return None

    def nodes_at_dist_k(self, A, k, ans=[]):
        if A is None:
            return []
        if k == 0:
            ans.append(A.val)
            return ans
        self.nodes_at_dist_k(A.left, k-1, ans)
        self.nodes_at_dist_k(A.right, k-1, ans)
        return ans

    def solve(self, A, B, C):
        ans = []
        path = []
        self.path_to_node(A, B, ans=path)
        ans = self.nodes_at_dist_k(path[0], C, ans=ans)
        C -= 1
        prev = path[0]
        for ele in path[1:]:
            if C == 0:
                ans.append(ele.val)
                return ans
            if ele.right == prev:
                self.nodes_at_dist_k(ele.left, C-1, ans)
            elif ele.left == prev:
                self.nodes_at_dist_k(ele.right, C-1, ans)
            C -= 1
            prev = ele
        return ans


if __name__ == "__main__":
    s = Solution()
    n1 = TreeNode(4)
    n2 = TreeNode(46)
    n3 = TreeNode(97)
    n1.left = n2
    n1.right = n3

    n4 = TreeNode(32)
    n5 = TreeNode(44)  # 6

    n2.left = n4
    n2.right = n5

    n6 = TreeNode(17)  # 12
    n7 = TreeNode(94)

    n3.left = n6
    n3.right = n7

    n8 = TreeNode(29)
    n9 = TreeNode(7)

    n10 = TreeNode(35)
    n11 = TreeNode(81)

    n4.left = n8
    n4.right = n9

    n5.left = n10
    n5.right = n11

    print(s.solve(n1, 7, 4))
