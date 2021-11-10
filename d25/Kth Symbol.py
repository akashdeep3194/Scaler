class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if A == 1:
            return 0
        sa = self.solve(A-1,(B+1)//2)
        if sa == 0:
            if B&1 == 0:
                return 1
            else:
                return 0
        if sa == 1:
            if B&1 == 0:
                return 0
            else:
                return 1

# s = Solution()
# print(s.solve(4,5))
