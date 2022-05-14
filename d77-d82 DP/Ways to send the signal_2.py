from sys import setrecursionlimit
setrecursionlimit(10**9)


class Solution:
    # @param A : integer
    # @return an integer

    def recfn(self, A, i, dp):
        z = 10**9+7
        if A == 1:
            return 1
        if dp[A-1][0] == -1:
            dp[A-1][0] = self.recfn(A-1, 0, dp)
        if i == 0:
            if dp[A-1][1] == -1:
                dp[A-1][1] = self.recfn(A-1, 1, dp)
            return (dp[A-1][1] + dp[A-1][0]) % z
        else:
            return dp[A-1][0] % z

    def solve(self, A):
        z = 10**9+7
        dp = [[-1 for _ in range(2)] for _ in range(A+1)]
        dp[1][0] = 1
        dp[1][1] = 1

        for i in range(2, A+1):
            for j in range(2):
                if j == 0:
                    dp[i][j] = (dp[i-1][j+1] + dp[i-1][j]) % z
                else:
                    dp[i][j] = dp[i-1][j-1]
        return (dp[A][0]+dp[A][1]) % z


if __name__ == '__main__':
    A = 99924
    s = Solution()
    print(s.solve(A))
