class Solution:
    # @param A : list of list of integers
    # @return an integer
    def recfn(self, A):
        dp = [-1 for _ in range(len(A)+1)]
        for i in range(len(A)):
            sa = 0
            for j in range(i):
                if A[j][1] < A[i][1] and A[j][0] < A[i][0]:
                    sa = max(sa, dp[j] + 1)
            dp[i] = sa

        return max(dp)

    def solve(self, A):
        A.sort()
        return self.recfn(A) + 1
