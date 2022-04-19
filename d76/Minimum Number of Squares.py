import sys
sys.setrecursionlimit(10**8)


class Solution:
    # @param A : integer
    # @return an integer
    def countMinSquares(self, A, dp=None):
        if not dp:
            dp = [-1 for _ in range(A+1)]
        if A == 0:
            return 0
        if A == 1:
            return 1

        ans = 2**32-1
        i = 1
        while i*i <= A:
            if dp[A-i*i] == -1:
                dp[A-i*i] = self.countMinSquares(A-i*i, dp)
            ans = min(ans, dp[A-i*i])
            i += 1
        ans += 1
        return ans


if __name__ == '__main__':
    A = 1200
    s = Solution()
    print(s.countMinSquares(A))
