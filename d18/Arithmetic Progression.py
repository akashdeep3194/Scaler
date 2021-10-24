class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A = sorted(A)
        if len(A)<2:
            return 0

        d = A[1] - A[0]

        for i in range(len(A)-1):
            ele =  A[i]
            if A[i+1] - ele != d:
                return 0
        return 1
