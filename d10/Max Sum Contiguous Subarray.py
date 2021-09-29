class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_sum = sum_till_now=A[0]
        for i in range(1,len(A)):
            sum_till_now += A[i]
            if sum_till_now<=A[i]:
                sum_till_now = A[i]
            max_sum = max(max_sum,sum_till_now)
        return max_sum


s=Solution()
print(s.maxSubArray([-1,2,-9,4,5,7]))
