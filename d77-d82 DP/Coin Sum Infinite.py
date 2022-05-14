class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def swap(self, dp):
        for i in range(len(dp)):
            dp[i][0], dp[i][1] = dp[i][1], dp[i][0]

    def recfn(self, A, B, dp):
        z = 10**6+7
        k = len(A)-1
        while k >= 0:
            for i in range(1, B+1):
                if i-A[k] >= 0:
                    dp[i][0] = (dp[i-A[k]][0] + dp[i][1]) % z
                else:
                    dp[i][0] = dp[i][1]
            self.swap(dp)
            k -= 1
        return (dp[B][-1]) % z

    def coinchange2(self, A, B):
        z = 10**6+7
        dp = [[-1 for _ in range(2)]for _ in range(B+1)]
        for i in range(B+1):
            dp[i][-1] = 0
        for j in range(2):
            dp[0][j] = 1

        answer = self.recfn(A, B, dp=dp) % z

        return answer


if __name__ == '__main__':
    A = [1, 2, 3]
    B = 4
    s = Solution()
    print(s.coinchange2(A, B))
