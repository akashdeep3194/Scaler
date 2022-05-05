from sys import setrecursionlimit as srl
srl(10**6)


class Solution:
    # @param A : string
    # @return an integer
    def recfn(self, A, si=0, dp=None):
        if not dp:
            dp = [0 for ele in range(len(A)+1)]
        if si == len(A):
            return 1
        if A[si] == "0":
            return 0
        if si == len(A) - 1:
            return 1

        ways_2 = 0
        if int(A[si:si+2]) < 27:
            if dp[si+2] == 0:
                dp[si+2] = self.recfn(A, si=si+2, dp=dp)
            ways_2 = dp[si+2]
        if dp[si+1] == 0:
            dp[si+1] = self.recfn(A, si=si+1, dp=dp)
        ways_1 = dp[si+1]

        return (ways_1 + ways_2) % (10**9+7)

    def numDecodings(self, A):
        dp = [0 for ele in range(len(A)+1)]
        dp[0] = self.recfn(A, dp=dp)
        return dp[0]


if __name__ == '__main__':
    A = "26110"
    s = Solution()
    print(len(A))
    print(s.numDecodings(A))
