class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        A.sort()
        B.sort()
        dist = 0
        for i in range(len(A)):
            dist = max(dist, abs(A[i]-B[i]))
        return dist
