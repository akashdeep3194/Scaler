class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : integer
    # @return an integer

    def recfn(self, A, B, C, D, i=0, dp=None):
        if i == len(A):
            return 0
        if D < 0:
            return 0

        if not dp:
            dp = [[-1 for _ in range(D+1)]for _ in range(len(A)+1)]

        ans1 = ans2 = 0

        if D-C[i] >= 0:
            if dp[i][D-C[i]] == -1:
                dp[i][D-C[i]] = self.recfn(A, B, C, D-C[i], i, dp)
            ans1 = dp[i][D-C[i]] + A[i]*B[i]

        if dp[i+1][D] == -1:
            dp[i+1][D] = self.recfn(A, B, C, D, i+1, dp)
        ans2 = dp[i+1][D]
        return max(ans1, ans2)

    def solve(self, A, B, C, D):
        return self.recfn(A, B, C, D)


if __name__ == '__main__':
    A = [2]
    B = [5]
    C = [10]
    D = 99
    s = Solution()
    print(s.solve(A, B, C, D))
