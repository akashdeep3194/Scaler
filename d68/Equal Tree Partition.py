# Definition for a  binary tree node
import sys
sys.setrecursionlimit(10**9)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solveH(self, A, B):
        if A is None:
            return 0, 0
        sl, ansl = self.solveH(A.left, B)
        sr, ansr = self.solveH(A.right, B)
        if ansl == 1 or ansr == 1:
            return -1, 1
        if A.val + sl == B or A.val + sr == B or A.val + sl + sr == B:
            return -1, 1
        else:
            return sl + sr + A.val, 0

    def total_sum(self, A):
        if A is None:
            return 0
        sl = self.total_sum(A.left)
        sr = self.total_sum(A.right)
        return sl + sr + A.val

    def solve(self, A):
        tsum = self.total_sum(A)
        if tsum % 2 != 0:
            return 0
        else:
            B = tsum//2
            return self.solveH(A, B)[1]


def deserialize(A):
    i = 0
    for ind, ele in enumerate(A):
        if A[ind] == -1:
            continue
        fci = (i+1)*2 - 1
        sci = (i+1)*2
        fc = A[fci]
        sc = A[sci]
        if i == 0:
            node = TreeNode(A[i])
            root = node
        else:
            node = A[ind]
        if fc != -1:
            fc = TreeNode(fc)
            node.left = fc
            A[fci] = fc
        if sc != -1:
            sc = TreeNode(sc)
            node.right = sc
            A[sci] = sc
        i += 1
    return root


if __name__ == "__main__":
    s = Solution()
    A = [375, 112, 267, -1, -1, 632, -1, -1, 157, 596, 633, -1, -1, -1, -1]
    root = deserialize(A)
    print(s.total_sum(root))
    print(s.solve(root))
