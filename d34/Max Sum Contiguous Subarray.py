class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        sm = 0
        ans = A[0]
        for ele in A:
            sm += ele
            ans = max(ans,sm)
            if sm<0:
                sm = 0
        return ans

# s = Solution()
# print(s.maxSubArray([1, 2, 3, 4, -10]))
