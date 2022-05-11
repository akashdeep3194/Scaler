from sys import setrecursionlimit
setrecursionlimit(10**6)


class Solution:
    # @param A : list of integers
    # @return an integer
    def mcm(self, arr, si, ei, dp=None):
        if not dp:
            dp = [[-1 for _ in range(len(arr)+1)] for _ in range(len(arr)+1)]
        if ei-si < 2:
            return 0
        if ei-si == 2:
            return arr[si]*arr[si+1]*arr[si+2]

        sa = 10**31
        for i in range(si+1, ei):
            if dp[i][ei] == -1:
                dp[i][ei] = self.mcm(arr, i, ei, dp)
            x = dp[i][ei]

            if dp[si][i] == -1:
                dp[si][i] = self.mcm(arr, si, i, dp)
            y = dp[si][i]

            sa = min(sa, x + y + arr[si]*arr[i]*arr[ei])
        return sa

    def solve(self, A):
        ans = self.mcm(A, si=0, ei=len(A)-1)
        return ans


if __name__ == '__main__':
    A = [45, 17, 34, 27, 12, 22]
    s = Solution()
    dp = dict()
    print(s.solve(A))
