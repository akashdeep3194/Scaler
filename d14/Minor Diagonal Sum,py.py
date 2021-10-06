class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        m = len(A[0])
        n = len(A)

        i = 0
        s = 0

        for i in range(n):
            s += A[i][i]

        return s
