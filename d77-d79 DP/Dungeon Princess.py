class Solution:
    # @param A : list of list of integers
    # @return an integer
    def calculateMinimumHP(self, A):
        dp = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
        dp[len(A)-1][len(A[0])-1] = max(1 - A[len(A)-1][len(A[0])-1], 1)

        i = len(A)-1
        for j in range(len(A[0])-2, -1, -1):
            dp[i][j] = max(dp[i][j+1] - A[i][j], 1)

        j = len(A[0])-1
        for i in range(len(A)-2, -1, -1):
            dp[i][j] = max(dp[i+1][j] - A[i][j], 1)

        i = len(A)-2
        j = len(A[0])-2
        while i >= 0:
            while j >= 0:
                dp[i][j] = max(1, min(dp[i][j+1], dp[i+1][j]) - A[i][j])
                j -= 1
            j = len(A[0])-2
            i -= 1
        return dp[0][0]


if __name__ == '__main__':
    A = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]
    s = Solution()
    print(s.calculateMinimumHP(A))
