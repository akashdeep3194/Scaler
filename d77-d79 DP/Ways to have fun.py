import sys
sys.setrecursionlimit(10**6)


class Solution:
    # @param A : integer
    # @return an integer

    def recfn(self, A, activity: str, dp):

        if A == 0:
            return 0
        if A == 1:
            return 1

        if activity == "P":
            if dp[A-1][1] == -1:
                dp[A-1][1] = self.recfn(A-1, "S", dp)

            if dp[A-1][2] == -1:
                dp[A-1][2] = self.recfn(A-1, "T", dp)

            ways_P = dp[A-1][1] + dp[A-1][2]

            return ways_P % (10**9+7)

        if activity == "T":
            if dp[A-1][0] == -1:
                dp[A-1][0] = self.recfn(A-1, "P", dp)

            if dp[A-1][1] == -1:
                dp[A-1][1] = self.recfn(A-1, "S", dp)

            if dp[A-2][2] == -1:
                dp[A-2][2] = self.recfn(A-2, "T", dp)
            ways_T = (dp[A-1][0] + dp[A-1][1]) % (10**9+7) - \
                2*dp[A-2][2] % (10**9+7)
            return ways_T % (10**9+7)

        if activity == "S":

            if dp[A-1][0] == -1:
                dp[A-1][0] = self.recfn(A-1, "P", dp)

            if dp[A-1][1] == -1:
                dp[A-1][1] = self.recfn(A-1, "S", dp)

            if dp[A-1][2] == -1:
                dp[A-1][2] = self.recfn(A-1, "T", dp)

            ways_S = (dp[A-1][0] + dp[A-1][1]) % (10**9+7) + dp[A-1][2]
            return ways_S % (10**9+7)

    def solve(self, A):
        dp = [[-1, -1, -1] for _ in range(A+1)]
        dp[A][0] = self.recfn(A, activity="P", dp=dp)
        dp[A][1] = self.recfn(A, activity="S", dp=dp)
        dp[A][2] = self.recfn(A, activity="T", dp=dp)
        return ((dp[A][0] + dp[A][1]) % (10**9+7) + dp[A][2]) % (10**9+7)


if __name__ == '__main__':
    A = 1
    s = Solution()
    print(s.solve(A))
