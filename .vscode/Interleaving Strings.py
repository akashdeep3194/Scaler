from numpy import dsplit


class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def recfn(self, A, B, C, i, j, k, dp=None):

        if not dp:
            dp = [[-1 for _ in range(len(B)+1)] for _ in range(len(A)+1)]

        if i >= len(A):
            if B[j:] == C[k:]:
                return 1
            else:
                return 0
        if j >= len(B):
            if A[i:] == C[k:]:
                return 1
            else:
                return 0

        if A[i] == B[j] == C[k]:
            if dp[i+1][j] == -1:
                dp[i+1][j] = self.recfn(A, B, C, i+1, j, k+1, dp)
            sa1 = dp[i+1][j]

            if dp[i][j+1] == -1:
                dp[i][j+1] = self.recfn(A, B, C, i, j+1, k+1, dp)
            sa2 = dp[i][j+1]

            return sa1 | sa2

        elif A[i] == C[k]:
            if dp[i+1][j] == -1:
                dp[i+1][j] = self.recfn(A, B, C, i+1, j, k+1, dp)
            sa1 = dp[i+1][j]
            return sa1
        elif B[j] == C[k]:
            if dp[i][j+1] == -1:
                dp[i][j+1] = self.recfn(A, B, C, i, j+1, k+1, dp)
            sa2 = dp[i][j+1]
            return sa2
        else:
            return 0

    def isInterleave(self, A, B, C):
        return self.recfn(A, B, C, i=0, j=0, k=0)


if __name__ == '__main__':
    A = "accbaabaaabbcbaacbababacaababbcbabaababcaabbbbbcacbaa" 
    B = "cabaabcbabcbaaaacababccbbccaaabaacbbaaabccacabaaccbbcbcb" 
    C ="accbcaaabbaabaaabbcbcbabacbacbababaacaaaaacbabaabbcbccbbabbccaaaaabaabcabbcaabaaabbcbcbbbcacabaaacccbbcbbaacb"
    s = Solution()
    print(s.isInterleave(A, B, C))
