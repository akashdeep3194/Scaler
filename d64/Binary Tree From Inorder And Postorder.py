

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        return self.buildTreeHelper(B, A, 0, len(A)-1, 0, len(B)-1)

    def buildTreeHelper(self, A, B, ps, pe, ins, ine):
        if ps > pe:
            return None
        root = A[pe]
        root = TreeNode(root)
        i = ins
        for i in range(ins, ine+1):
            if root.val == B[i]:
                break
        ctrl = i - ins
        psl = ps
        pel = ps + ctrl - 1
        insl = ins
        inel = i - 1

        psr = pel + 1
        per = pe - 1
        insr = i + 1
        iner = ine

        lst = self.buildTreeHelper(A, B, psl, pel, insl, inel)
        rst = self.buildTreeHelper(A, B, psr, per, insr, iner)
        root.left = lst
        root.right = rst

        return root


def print_tree(root):
    if root is None:
        return

    print_tree(root.left)
    print_tree(root.right)
    print(root.val)


if __name__ == "__main__":
    s = Solution()
    A = [2, 1, 3]
    B = [2, 3, 1]

    root = s.buildTree(A, B)
    print_tree(root)
