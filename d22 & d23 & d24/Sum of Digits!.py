import sys
sys.setrecursionlimit(10**5)

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A//10 == 0:
            return A
        sa = self.solve(A//10)
        return sa + A%10

# s = Solution()
# print(s.solve(123))
