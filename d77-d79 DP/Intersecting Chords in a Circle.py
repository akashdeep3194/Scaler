from sys import setrecursionlimit
setrecursionlimit(10**6)


class Solution:
    # @param A : integer
    # @return an integer

    def recfn(self, A, dp=None):
        z = 10**9+7
        if not dp:
            dp = [-1 for _ in range(2*A+1)]

        if A <= 1:
            return 1

        sm = 0

        for i in range(A):
            if dp[A-(i+1)] == -1:
                dp[A-(i+1)] = self.recfn(A-(i+1), dp)
            x = dp[A-(i+1)]

            if dp[i] == -1:
                dp[i] = self.recfn(i, dp)
            y = dp[i]

            sm = (sm+(x*y) % z) % z

        return sm % z

    def chordCnt(self, A):
        return self.recfn(A)


if __name__ == '__main__':
    A = 3
    s = Solution()
    print(s.chordCnt(A))
