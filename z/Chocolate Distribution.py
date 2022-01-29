import sys
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        if B == 0:
            return 0
        i = 0
        j = B-1
        ans = sys.maxsize
        if B>len(A):
            if len(A) == 0:
                return 0
            ans = A[-1]
            return ans
        while j<len(A):
            ans = min(ans,A[j]-A[i])
            j += 1
            i += 1
        return ans
