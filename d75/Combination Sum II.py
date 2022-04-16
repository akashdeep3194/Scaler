class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def recfn(self, A, B, si, ans, li):
        if B == 0:
            if li not in ans:
                ans.append(li.copy())
            return
        elif B < 0:
            return
        elif si >= len(A):
            return
        li.append(A[si])
        self.recfn(A, B-A[si], si+1, ans, li)
        li.pop()
        self.recfn(A, B, si+1, ans, li)

        return

    def combinationSum(self, A, B):
        A.sort()
        answer = []
        li = []
        self.recfn(A, B, 0, answer, li)
        return answer


if __name__ == '__main__':
    A = []
    s = Solution()
    A = [10, 1, 2, 7, 6, 1, 5]
    B = 8
    print(s.combinationSum(A, B))
