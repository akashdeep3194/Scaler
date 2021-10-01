class Solution:
    # @param A : list of integers
     # @return an long
    def subarraySum(self, A):

        s = 0

        for i in range(len(A)):
            s += A[i]*(i+1)*(len(A)-i)

        return s

# s = Solution()
# print(s.subarraySum([1, 2, 3]))
