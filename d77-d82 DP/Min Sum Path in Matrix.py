class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        dp = [[0 for _ in range(len(A[0]))]for _ in range(len(A))]

        i = 0
        prev = 0
        for j in range(len(A[0])):
            dp[i][j] = A[i][j] + prev
            prev = dp[i][j]

        j = 0
        prev = dp[0][0]
        for i in range(1, len(A)):
            dp[i][j] = A[i][j] + prev
            prev = dp[i][j]

        for i in range(1, len(A)):
            for j in range(1, len(A[0])):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + A[i][j]
        return dp[-1][-1]


if __name__ == '__main__':
    A = [
        [1, 3, 2],
        [4, 3, 1],
        [5, 6, 1],
    ]
    s = Solution()
    print(s.minPathSum(A))
