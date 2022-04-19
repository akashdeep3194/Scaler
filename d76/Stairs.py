class Solution:
    # @param A : integer
    # @return an integer

    def climbStairs(self, A, dp=None):
        if not dp:
            dp = [-1 for _ in range(A+1)]

        if A == 1:
            dp[1] = 1
            return 1
        if A == 2:
            dp[2] = 2
            return 2

        if dp[A-1] == -1:
            dp[A-1] = self.climbStairs(A-1, dp)
        if dp[A-2] == -1:
            dp[A-2] = self.climbStairs(A-2, dp)

        return dp[A-1]+dp[A-2]


if __name__ == '__main__':
    A = 36
    s = Solution()
    print(s.climbStairs(A))
