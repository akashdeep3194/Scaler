class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        i = 0
        ans = 0
        j = len(A)-1
        while j > i:
            sa = min(A[j], A[i])*(j-i)
            ans = max(ans, sa)
            if A[i] < A[j]:
                i += 1
            else:
                j -= 1
        return ans
