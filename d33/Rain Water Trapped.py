class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        right_max = []
        rmax = A[-1]
        for ele in A[::-1]:
            rmax = max(rmax,ele)
            right_max.append(rmax)
        right_max = right_max[::-1]

        lmax = A[0]
        water = 0
        for i,ele in enumerate(A):
            lmax = max(lmax,ele)
            water += max(min(right_max[i],lmax) - ele,0)

        return water

# s = Solution()
# A = [ 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 ]
# print(s.trap(A))
