from sys import setrecursionlimit
setrecursionlimit(10**6)


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def recfn(self, B, C, cap, i, dp):
        if cap == 0:
            return 0
        if i == len(B):
            return 10**31
        ans1 = ans2 = 10**31
        if cap-B[i] >= 0:
            if dp[i][cap-B[i]] == -1:
                dp[i][cap-B[i]] = self.recfn(B, C, cap-B[i], i, dp)
            ans1 = dp[i][cap-B[i]]+C[i]

        if dp[i+1][cap] == -1:
            dp[i+1][cap] = self.recfn(B, C, cap, i+1, dp)
        ans2 = dp[i+1][cap]

        return min(ans1, ans2)

    def solve(self, A, B, C):
        maxc = max(A)
        dp = [[-1 for _ in range(maxc+1)]for _ in range(len(B)+1)]
        ans = 0
        for ele in A:
            ans += self.recfn(B, C, ele, i=0, dp=dp)
        return ans


if __name__ == '__main__':
    A = [2, 4, 6]
    B = [2, 1, 3]
    C = [2, 5, 3]
    s = Solution()
    print(s.solve(A, B, C))
