from sys import setrecursionlimit
setrecursionlimit(10**6)


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer

    def recfn(self, A, B, i, j, dp):
        if i == -1 or j == -1:
            return 0
        if A[i] == B[j]:
            if dp[i][j] == -1:
                dp[i][j] = self.recfn(A, B, i-1, j-1, dp) + 1
            return dp[i][j]
        else:
            if dp[i-1][j] == -1:
                dp[i-1][j] = self.recfn(A, B, i-1, j, dp)
            if dp[i][j-1] == -1:
                dp[i][j-1] = self.recfn(A, B, i, j-1, dp)

        return max(dp[i-1][j], dp[i][j-1])

    def solve(self, A, B):
        dp = [[-1 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
        return self.recfn(A, B, len(A)-1, len(B)-1, dp)


if __name__ == '__main__':
    A = "bebdeeedaddecebbbbbabebedc"
    B = "abaaddaabbedeedeacbcdcaaed"
    s = Solution()

    ans = (s.solve(A, B))
    print(ans)
