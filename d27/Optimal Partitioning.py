import sys
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        mn = sys.maxsize
        for i in range(len(A)-1):
            mn = min(A[i+1]-A[i],mn)
        return mn