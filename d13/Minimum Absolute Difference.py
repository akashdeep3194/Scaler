import sys
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A = sorted(A)
        d = sys.maxsize
        for i in range(len(A)-1):
            ele = A[i]
            d = min(d,abs(ele-A[i+1]))
        return d

# s = Solution()
# print(s.solve([1,2,3,4,6,0,5]))
