import sys

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):

        final_max = 0
        max_till_now = -1*sys.maxsize
        max_sum = 0

        for i,ele in enumerate(A):
            max_sum += ele
            max_till_now = max(max_till_now,max_sum)
            if max_sum <= 0:
                max_sum = 0
        return max_till_now

# s = Solution()
# A = [1, 2, 3, 4, -10,3,-1,9]
# print(s.maxSubArray(A))
