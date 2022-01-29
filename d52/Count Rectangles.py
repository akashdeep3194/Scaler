class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        dcxy = dict()
        for i in range(len(A)):
            dcxy[(A[i], B[i],)] = 1
