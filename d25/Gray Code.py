from math import log2

class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):

        if A == 0:
            return []
        if A == 1:
            return [0,1]

        sa = self.grayCode(A-1)
        k = len(sa)
        for i in range(k-1,-1,-1):
            sa.append(k+sa[i])
        return sa
        
# s = Solution()
# print(s.grayCode(3))
