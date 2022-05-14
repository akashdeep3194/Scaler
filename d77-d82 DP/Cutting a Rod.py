from sys import setrecursionlimit
setrecursionlimit(10**6)


class Solution:
    # @param A : list of integers
    # @return an integer
    def recfn(self, A, l, i, dp=None):
        if not dp:
            dp = [[-1 for _ in range(len(A))] for _ in range(len(A)+1)]
        if i == l-1:
            return max(A[l-1], A[0]+A[i-1])
        if dp[l-i][1] == -1:
            dp[l-i][1] = self.recfn(A, l-i, 1, dp)
        ans1 = dp[l-i][1] + A[i-1]

        if dp[l][i+1] == -1:
            dp[l][i+1] = self.recfn(A, l, i+1, dp)
        ans2 = dp[l][i+1]

        return max(ans1, ans2)

    def solve(self, A):
        return self.recfn(A, len(A), i=1)


if __name__ == '__main__':
    A = [3, 4, 1, 6, 2]
    s = Solution()
    print(s.solve(A))
