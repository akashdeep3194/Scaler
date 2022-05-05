class Solution:
    # @param A : integer
    # @return an integer

    def recfn(self, A, dp=None):
        if A == 0:
            return 1
        if A == 1:
            return 1
        if not dp:
            dp = [-1 for _ in range(A+1)]
        sm = 0
        i = 1
        while A-i >= 0 and i <= 6:
            if dp[A-i] == -1:
                dp[A-i] = self.recfn(A-i, dp)
            sm = (sm + dp[A-i]) % (10**9+7)
            i += 1
        return sm

    def solve(self, A):
        return self.recfn(A)


if __name__ == '__main__':
    A = 25
    s = Solution()
    print(s.solve(A))
