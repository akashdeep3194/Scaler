class Node():
    def __init__(self, val, left=None, right=None) -> None:
        self.left = left
        self.right = right
        self.val = val


def path(root, N, ans):
    if root is None:
        return 0
    if root == N:
        ans.append(root)
        return 1
    else:
        la = path(root.left, N, ans)
        ra = path(root.right, N, ans)

        if la == 1:
            ans.append(root)
            return 1
        elif ra == 1:
            ans.append(root)
            return 1
        else:
            return 0


def LCA(root, arr):
    N1 = arr[0]
    N2 = arr[1]
    path1 = []
    path2 = []
    lca_node = root
    path(root, N1, path1)
    path(root, N2, path2)
    path1 = path1[::-1]
    path2 = path2[::-1]

    for i in range(len(path1)):
        if path1[i] != path2[i]:
            lca_node = path1[i-1]
            break
    return lca_node


if __name__ == "__main__":
    n1 = Node(5)
    n2 = Node(7)
    n3 = Node(9)
    n4 = Node(12)
    n5 = Node(14, n2, n1)
    n6 = Node(15, n4, n3)
    n7 = Node(7, n6, n5)

    ans = LCA(n7, [n2, n3])
    print(ans.val)

# Tree
#       7
#  15         14
# 12 9      7 5
