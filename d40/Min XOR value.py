import sys
class Solution:    
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        A.sort()
        ans = sys.maxsize
        for i in range(len(A)-1):
            ele = A[i]
            ans = min(ele^A[i+1], ans)
        return ans
