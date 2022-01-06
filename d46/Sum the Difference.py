class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        ans = 0
        for i in range(len(A)):
            for j in range(len(A)-1, i, -1):
                ans = (ans + (A[j]-A[i])*((2**(j-i-1)) %
                       (10**9+7))) % (10**9+7)
        return ans
