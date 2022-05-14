class Solution:
    # @param A : string
    # @return an integer
    def expandpallindrome(self, A, dp):
        for i in range(len(A)):
            dp[i][i] = 1

            j = i-1
            k = i+1

            while j >= 0 and k < len(A):
                if A[j] == A[k]:
                    dp[j][k] = 1
                else:
                    break
                j -= 1
                k += 1
        for i in range(len(A)):
            j = i
            k = i+1

            while j >= 0 and k < len(A):
                if A[j] == A[k]:
                    dp[j][k] = 1
                else:
                    break
                j -= 1
                k += 1

    def minCut(self, A):
        dp = [[-1 for _ in range(len(A)+1)] for _ in range(len(A)+1)]
        if len(A) == 1:
            return 0
        self.expandpallindrome(A, dp)
        return self.minCutr(A, si=0, ei=len(A)-1, dp=dp)

    def minCutr(self, A, si, ei, dp, dpm=None):
        if not dpm:
            dpm = [0 for _ in range(len(A)+1)]
            dpm[-1] = -1
            dpm[-2] = 0

        for j in range(len(dpm)-2, -1, -1):
            for i in range(len(dp[0])-1, -1, -1):
                if dp[j][i] == 1:
                    break
            dpm[j] = min(dpm[j+1] + 1, dpm[i+1] + 1)
        return dpm[0]


if __name__ == '__main__':
    A = "aabac"
    s = Solution()
    print(s.minCut(A))
