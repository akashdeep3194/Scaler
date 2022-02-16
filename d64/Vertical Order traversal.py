from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, A):
        q = Queue()
        q.put((A, 0))
        q.put(None)
        minl = 0
        maxl = 0
        dc = dict()
        dc[0] = [A]
        while q.qsize() > 1:
            ele = q.get()
            if ele == None:
                q.put(ele)
                continue
            else:
                if ele[0].left is not None:
                    q.put((ele[0].left, ele[1]-1))
                    if ele[1]-1 < minl:
                        minl = ele[1]-1
                    li = dc.get(ele[1]-1, [])
                    li.append(ele[0].left)
                    dc[ele[1]-1] = li

                if ele[0].right is not None:
                    q.put((ele[0].right, ele[1]+1))
                    if ele[1]+1 > maxl:
                        maxl = ele[1]+1
                    li = dc.get(ele[1]+1, [])
                    li.append(ele[0].right)
                    dc[ele[1]+1] = li
        ans = []
        for i in range(minl, maxl+1):
            arr = []
            for ele in dc[i]:
                arr.append(ele.val)
            ans.append(arr)
        return ans


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    n2 = TreeNode(4)
    n3 = TreeNode(9)
    n4 = TreeNode(10)
    n5 = TreeNode(12)
    n6 = TreeNode(15)

    root.left = n2
    root.right = n3
    n2.left = n4
    n2.right = n5
    n5.right = n6

    print(s.verticalOrderTraversal(root))


#        3
#     4      9
# 10    12
#          15
