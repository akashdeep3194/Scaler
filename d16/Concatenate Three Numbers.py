class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        li = sorted([A,B,C])
        return li[0]*10000+li[1]*100+li[2]*1

# s = Solution()
# print(s.solve(30,30,10))
