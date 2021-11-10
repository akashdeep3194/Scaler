class Solution:
    # @param A : integer
    # @return an integer
    def solveh(self,A):
        if A//10 == 0:
            return A
        sa = self.solveh(A//10)
        ans = sa + A%10
        if ans>9:
            ans = self.solveh(ans)
        return ans

    def solve(self, A):
        if self.solveh(A) == 1:
            return 1
        else:
            return 0

# s = Solution()
# print(s.solve(83557))
