class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):

        dp = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]

        y = 1
        for j in range(len(A[0])):
            if A[0][j] != 1:
                dp[0][j] = y
            else:
                y = 0
                dp[0][j] = 0
        x = 1
        for i in range(len(A)):
            if A[i][0] != 1:
                dp[i][0] = x
            else:
                x = 0
                dp[i][0] = 0

        for i in range(1, len(A)):
            for j in range(1, len(A[0])):
                if A[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        return dp[-1][-1]


if __name__ == '__main__':
    A = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0],
    ]
    s = Solution()
    print(s.uniquePathsWithObstacles(A))
