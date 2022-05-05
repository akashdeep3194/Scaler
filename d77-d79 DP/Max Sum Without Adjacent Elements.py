import sys
sys.setrecursionlimit(10**6)


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def __init__(self) -> None:
        self.ans = 0
        self.sm = 0

    def unselect(self, A, B, i, j):
        if i+1 < len(A):
            B[i+1][j] = A[i+1][j]
        if j+1 < len(A[0]):
            B[i][j+1] = A[i][j+1]
        if i-1 >= 0:
            B[i-1][j] = A[i-1][j]
        if j-1 >= 0:
            B[i][j-1] = A[i][j-1]
        if i-1 >= 0 and j-1 >= 0:
            B[i-1][j-1] = A[i-1][j-1]
        if i-1 >= 0 and j+1 < len(A[0]):
            B[i-1][j+1] = A[i-1][j+1]
        if i+1 < len(A) and j-1 >= 0:
            B[i-1][j-1] = A[i-1][j-1]
        if i+1 < len(A) and j+1 < len(A[0]):
            B[i+1][j+1] = A[i+1][j+1]

    def select(self, A, B, i, j):
        if i+1 < len(A):
            B[i+1][j] = -1
        if j+1 < len(A[0]):
            B[i][j+1] = -1
        if i-1 >= 0:
            B[i-1][j] = -1
        if j-1 >= 0:
            B[i][j-1] = -1
        if i-1 >= 0 and j-1 >= 0:
            B[i-1][j-1] = -1
        if i-1 >= 0 and j+1 < len(A[0]):
            B[i-1][j+1] = -1
        if i+1 < len(A) and j-1 >= 0:
            B[i-1][j-1] = -1
        if i+1 < len(A) and j+1 < len(A[0]):
            B[i+1][j+1] = -1
        return

    def recfn(self, A, B, i, j):
        for i in range(i, len(A)):
            for j in range(j, len(A[0])):
                if B[i][j] != -1:
                    self.sm += A[i][j]
                    tmp = copy.deepcopy(B)
                    self.select(A, B, i, j)
                    self.recfn(A, B, i, j+1)

                    self.sm -= A[i][j]
                    B = copy.deepcopy(tmp)
                    self.recfn(A, B, i, j+1)
            if i != len(A)-1:
                j = 0
        self.ans = max(self.sm, self.ans)
        return

    def adjfn(self, A, sj=0, dp=None):
        if not dp:
            dp = [-1 for _ in range(len(A[0])+2)]

        if sj >= len(A[0]):
            return 0

        if dp[sj+2] == -1:
            dp[sj+2] = self.adjfn(A, sj+2, dp)

        ans_1 = dp[sj+2] + A[0][sj]
        ans_2 = dp[sj+2] + A[0+1][sj]

        if dp[sj+1] == -1:
            dp[sj+1] = self.adjfn(A, sj+1, dp)
        ans_3 = dp[sj+1]

        ans = max(ans_1, ans_2, ans_3)
        self.ans = max(self.ans, ans)

        return ans

    def adjacent(self, A):
        # B = copy.deepcopy(A)
        # self.recfn(A, B, 0, 0)
        self.adjfn(A)
        return self.ans


if __name__ == '__main__':
    A = [
        [8, 2, 15, 14, 17, 8, 6, 16, 12, 11, 19, 19, 19, 6, 6, 1, 5, 9, 2],
        [18, 11, 14, 14, 4, 6, 14, 15, 14, 3, 17, 18, 16, 13, 5, 20, 6, 16, 5]
    ]
    # A = [
    #     [1, 2, 3, 4],
    #     [2, 3, 4, 5]
    # ]
    s = Solution()
    print(s.adjacent(A))
