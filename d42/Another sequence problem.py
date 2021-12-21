class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A,dp = {}):
        if A == 0 or A == 1:
            return 1
        if A == 2:
            return 2

        si1 = A-1
        si2 = A-2
        si3 = A-3

        if dp.get(A-1,-1) == -1:
            sa1 = self.solve(si1,dp)
            dp[si1] = sa1
        else:
            sa1 = dp[si1]

        if dp.get(si2,-1) == -1:
            sa2 = self.solve(si2,dp)
            dp[si2] = sa2
        else:
            sa2 = dp[si2]

        if dp.get(si3,-1) == -1:
            sa3 = self.solve(si3,dp)
            dp[si3] = sa3
        else:
            sa3 = dp[si3]

        ans = sa1 + sa2 + sa3 + A

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.solve(4))
