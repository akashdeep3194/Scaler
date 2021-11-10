class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 1 or A == 0:
            return 1
        sa = self.solve(A-1)
        return sa*A
# s = Solution()
# print(s.solve(4))
