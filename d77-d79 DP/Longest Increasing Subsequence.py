from sys import setrecursionlimit
setrecursionlimit(10**6)


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def __init__(self) -> None:
        self.l = 0
        self.ans = 0

    def recfn(self, A, si, num=-1, numi=-1, dp=None):
        if not dp:
            dp = [[-1 for _ in range(len(A)+2)] for _ in range(len(A)+2)]
        if si == len(A):
            dp[si][numi] = 0
            return 0

        ans_1 = 0

        if A[si] > num:
            if dp[si+1][si] == -1:
                dp[si+1][si] = self.recfn(A, si+1, A[si], numi=si, dp=dp) + 1
            ans_1 = dp[si+1][si]

        if dp[si+1][numi] == -1:
            dp[si+1][numi] = self.recfn(A, si+1, num, numi=numi, dp=dp)
        ans_2 = dp[si+1][numi]

        return max(ans_1, ans_2)

    def lis(self, A):
        return self.recfn(A, 0)


if __name__ == '__main__':
    A = [54, 19, 51, 16, 54, 64]
    s = Solution()
    print(s.lis(A))
