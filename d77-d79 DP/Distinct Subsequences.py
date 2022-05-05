import time


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def recfn(self, A, B, i, j):
        if i < j:
            return 0
        if A[:i+1] == B[:j+1]:
            return 1
        if j == -1:
            return 1

        if A[i] == B[j]:
            ans1 = self.recfn(A, B, i-1, j-1)
            ans2 = self.recfn(A, B, i-1, j)
            return ans1 + ans2
        else:
            ans3 = self.recfn(A, B, i-1, j)
            return ans3

    def iterfn(self, A, B):
        dp = [[-1 for _ in range(len(B)+1)] for _ in range(len(A)+1)]

        for j in range(1, len(B)+1):
            #
            #
            dp[0][j] = 0
        for i in range(len(A)+1):
            dp[i][0] = 1
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

    def numDistinct(self, A, B):

        return self.recfn(A, B, len(A)-1, len(B)-1)


if __name__ == '__main__':
    A = "qanabopcbabcbabkdsjfbcabacbmcbbapcbabcbabcbabbadfbcbakjfhabcakjsdhfcababcbmnbabcbbabbcbcbabacbdkfjbksjfhbdcacbdkjbfcac"
    B = "abcabbaac"
    s = Solution()
    s1 = time.time()
    print(s.numDistinct(A, B))
    e1 = time.time()
    print(s.iterfn(A, B))
    e2 = time.time()
    print(str(e1-s1)+"\n"+str(e2-e1))
