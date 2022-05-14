from sys import setrecursionlimit
setrecursionlimit(10**6)


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def recfn(self, A, B, cap, i, dp=None):
        if dp is None:
            dp = [[-1 for _ in range(len(A)+1)] for _ in range(cap+1)]
        if i == len(A):
            return 0
        if cap == 0:
            return 0
        ans_1 = ans_2 = 0
        if cap >= B[i]:
            if dp[cap-B[i]][i+1] == -1:
                dp[cap-B[i]][i+1] = self.recfn(A, B, cap-B[i], i+1, dp)
            ans_1 = dp[cap-B[i]][i+1] + A[i]
        if dp[cap][i+1] == -1:
            dp[cap][i+1] = self.recfn(A, B, cap, i+1, dp)
        ans_2 = dp[cap][i+1]

        return max(ans_1, ans_2)

    def solve(self, A, B, C):
        return self.recfn(A, B, C, i=0)


if __name__ == '__main__':
    A = [60, 100, 120]
    B = [10, 20, 30]
    C = 50
    s = Solution()
    print(s.solve(A, B, C))
