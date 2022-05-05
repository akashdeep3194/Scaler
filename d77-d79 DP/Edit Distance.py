class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def recfn(self, A, B, i, j, dp):
        if i == -1:
            return j+1
        if j == -1:
            return i+1
        if A[i] == B[j]:
            if dp[i][j] == -1:
                dp[i][j] = self.recfn(A, B, i-1, j-1, dp)
            return dp[i][j]
        else:
            if dp[i][j] == -1:
                dp[i][j] = self.recfn(A, B, i-1, j-1, dp)
            if dp[i][j+1] == -1:
                dp[i][j+1] = self.recfn(A, B, i-1, j, dp)
            if dp[i+1][j] == -1:
                dp[i+1][j] = self.recfn(A, B, i, j-1, dp)
            return min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1

    def minDistance(self, A, B):
        dp = [[-1 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
        return self.recfn(A, B, i=len(A)-1, j=len(B)-1, dp=dp)


if __name__ == '__main__':
    A = "Anshuman"
    B = "Antihuman"
    s = Solution()
    print(s.minDistance(A, B))
