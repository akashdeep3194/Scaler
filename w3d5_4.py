class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        maxn = 1
        minn = 2
        for ele in A:
            if ele % 2 == 0:
                if ele > maxn or maxn == 1:
                    maxn = ele
            else:
                if ele < minn or minn == 2:
                    minn = ele
        return maxn - minn


s = Solution()

print(s.solve([-10, -4, 3, -4, 2]))
