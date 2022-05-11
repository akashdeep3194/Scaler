from sys import setrecursionlimit
setrecursionlimit(10**6)


class Solution:
    # @param A : string
    # @return an integer
    def recfn(self, A, B, i=0, j=0, dp=None):
        if not dp:
            dp = [[-1 for i in range(len(A)+1)]for _ in range(len(B)+1)]

        if i >= len(A) or j >= len(B):
            return 0

        if A[i] == B[j]:
            if dp[i+1][j+1] == -1:
                dp[i+1][j+1] = self.recfn(A, B, i+1, j+1, dp)
            ans = dp[i+1][j+1] + 1
            return ans
        else:
            if dp[i+1][j] == -1:
                dp[i+1][j] = self.recfn(A, B, i+1, j, dp)
            ans1 = dp[i+1][j]
            if dp[i][j+1] == -1:
                dp[i][j+1] = self.recfn(A, B, i, j+1, dp)
            ans2 = dp[i][j+1]
            return max(ans1, ans2)

    def solve(self, A):
        B = A[::-1]
        return self.recfn(A, B)


if __name__ == '__main__':
    A = "bebeeed"
    s = Solution()
    print(s.solve(A))
