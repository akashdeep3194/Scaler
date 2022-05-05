from sys import setrecursionlimit
setrecursionlimit(10**8)


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def recfn(self, A, B, i, j, dp):
        if i == -1 and j == -1:
            return True
        if j == -1:
            return False
        if i == -1:
            if B[j] == "*":
                if dp[i+1][j] == -1:
                    dp[i+1][j] = self.recfn(A, B, i, j-1, dp)
                return dp[i+1][j]
            else:
                return False

        if A[i] == B[j] or B[j] == "?":
            if dp[i][j] == -1:
                dp[i][j] = self.recfn(A, B, i-1, j-1, dp)
            return dp[i][j]

        if B[j] == "*":
            if dp[i+1][j] == -1:
                dp[i+1][j] = self.recfn(A, B, i, j-1, dp)
            if dp[i][j+1] == -1:
                dp[i][j+1] = self.recfn(A, B, i-1, j, dp)

            return dp[i][j+1] or dp[i+1][j]

        if A[i] != B[j]:
            return False

    def iterfn(self, A, B, i=0, j=0):
        dp = [[-1 for _ in range(len(B)+1)]for _ in range(len(A)+1)]
        dp[0][0] = True

        for i in range(1, len(dp)):
            dp[i][0] = False
        i = 0
        found_char = 0
        for j in range(1, len(dp[0])):
            if B[j-1] == "*" and found_char == 0:
                dp[i][j] = True
            else:
                dp[i][j] = False
                found_char = 1

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if B[j-1] == "?" or B[j-1] == A[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif B[j-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                elif B[j-1] != A[i-1]:
                    dp[i][j] = False
        return dp[len(A)][len(B)], dp

    def isMatch(self, A, B):
        C = B[0]
        for ind in range(1, len(B)):
            if B[ind] == "*" and B[ind-1] == "*":
                continue
            else:
                C = C + B[ind]
        dp = [[-1 for _ in range(len(C)+1)]for _ in range(len(A)+1)]
        print(C)
        val, dp = self.iterfn(A, C)
        if val:
            return 1
        else:
            return 0


if __name__ == '__main__':
    # A = "aaa"
    # B = "a*"
    # A = "acz"
    # B = "a?a"
    # A = "cc"
    # B = "***??"
    A = "bcaccbabaa"
    B = "bb***c?c*?"
    s = Solution()
    print(s.isMatch(A, B))
    # print(s.iterfn(A, B, i=0, j=0))
